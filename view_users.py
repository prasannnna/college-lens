import sqlite3

conn = sqlite3.connect('database/app.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.execute("SELECT * FROM colleges")
print(cursor.fetchall())

cursor.execute("SELECT * FROM placements")
print(cursor.fetchall())

cursor.execute("SELECT * FROM college_details")
print(cursor.fetchall())

conn.close()
