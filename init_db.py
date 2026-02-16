import sqlite3

conn = sqlite3.connect('database/app.db')
cursor = conn.cursor()

with open('database/schema.sql') as f:
    cursor.executescript(f.read())
    
conn.commit()
conn.close()

print("Intialized Database Successfully")
