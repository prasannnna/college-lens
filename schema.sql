CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS colleges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    place TEXT NOT NULL,
    country TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS placements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    placed_students INTEGER,
    total_students INTEGER,
    FOREIGN KEY (college_id) REFERENCES colleges(id)
);

CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    company_name TEXT NOT NULL,
    FOREIGN KEY (college_id) REFERENCES colleges(id)
);

CREATE TABLE IF NOT EXISTS college_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER NOT NULL,
    fee INTEGER NOT NULL,
    hostel_rating INTEGER NOT NULL,
    cutoff_l INTEGER NOT NULL,
    cutoff_h INTEGER NOT NULL,
    placements_all INTEGER NOT NULL,
    hostel_food_rating INTEGER NOT NULL,
    top_branch TEXT NOT NULL,
    FOREIGN KEY (college_id) REFERENCES colleges(id)
);

CREATE TABLE IF NOT EXISTS branches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER NOT NULL,
    branch_name TEXT NOT NULL,
    intake INTEGER NOT NULL,
    cutoff_rank INTEGER,
    branch_rating REAL,
    faculty_rating REAL,
    FOREIGN KEY (college_id) REFERENCES colleges(id)
);

CREATE TABLE IF NOT EXISTS branch_placements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER NOT NULL,
    branch_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    total_students INTEGER NOT NULL,
    placed_students INTEGER NOT NULL,
    avg_package REAL,
    highest_package REAL,
    FOREIGN KEY (college_id) REFERENCES colleges(id),
    FOREIGN KEY (branch_id) REFERENCES branches(id)
);

