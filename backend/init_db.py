import sqlite3

conn = sqlite3.connect('../database/student_dashboard.db')  # <-- matches app.py
with open('../database/init.sql', 'r') as f:
    conn.executescript(f.read())
conn.close()
print("Database initialized.")