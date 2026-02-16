import os
import sqlite3

from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "venn_flask_secret_key_123")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "app.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")


def get_db_connection():
    os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db_if_not_exists():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table = cursor.fetchone()

    if not table:
        print("⚡ Creating database tables...")
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        print(" Tables created successfully")

    conn.close()


@app.route("/")
def mainpage():
    return render_template("mainpage.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            return redirect("/home")
        else:
            return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirmpassword = request.form["confirmpassword"]

        if password != confirmpassword:
            return render_template("signup.html", error="Passwords do not match")

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name, email, hashed_password),
            )
            conn.commit()
            conn.close()
            return redirect("/login")

        except sqlite3.IntegrityError:
            conn.close()
            return render_template("signup.html", error="Email already exists")

    return render_template("signup.html")


@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect("/login")

    return render_template("home.html", name=session["user_name"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/explore")
def explore():
    college_type = request.args.get("type")

    conn = get_db_connection()
    cursor = conn.cursor()

    if college_type:
        cursor.execute("SELECT * FROM colleges WHERE type = ?", (college_type,))
    else:
        cursor.execute("SELECT * FROM colleges")

    colleges = cursor.fetchall()
    conn.close()

    return render_template("explore.html", colleges=colleges)


@app.route("/college/<int:college_id>")
def college_dashboard(college_id):
    selected_branch = request.args.get("branch")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM colleges WHERE id = ?", (college_id,))
    college = cursor.fetchone()

    if not college:
        conn.close()
        return render_template("404.html"), 404

    cursor.execute(
        "SELECT * FROM placements WHERE college_id = ? ORDER BY year DESC",
        (college_id,),
    )
    placements = cursor.fetchall()

    cursor.execute(
        "SELECT year, company_name FROM companies WHERE college_id = ? ORDER BY year DESC",
        (college_id,),
    )
    companies = cursor.fetchall()

    cursor.execute(
        """
        SELECT fee, hostel_rating, cutoff_l, cutoff_h, placements_all,
               hostel_food_rating, top_branch
        FROM college_details
        WHERE college_id = ?
        """,
        (college_id,),
    )
    collegedetails = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM branches WHERE college_id = ? ORDER BY branch_name ASC",
        (college_id,),
    )
    branches = cursor.fetchall()

    branch_details = None
    branch_placements = []

    if selected_branch:
        cursor.execute(
            "SELECT * FROM branches WHERE college_id = ? AND branch_name = ?",
            (college_id, selected_branch),
        )
        branch_details = cursor.fetchone()

        if branch_details:
            cursor.execute(
                """
                SELECT * FROM branch_placements
                WHERE college_id = ? AND branch_id = ?
                ORDER BY year DESC
                """,
                (college_id, branch_details["id"]),
            )
            branch_placements = cursor.fetchall()

    conn.close()

    return render_template(
        "college_dashboard.html",
        college=college,
        placements=placements,
        companies=companies,
        collegedetails=collegedetails,
        branches=branches,
        selected_branch=selected_branch,
        branch_details=branch_details,
        branch_placements=branch_placements,
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


init_db_if_not_exists()

if __name__ == "__main__":
    app.run()
