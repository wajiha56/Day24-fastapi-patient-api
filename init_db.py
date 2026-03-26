import sqlite3

# Database connect karo
conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

# Table create karo agar exist na kare
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    fee REAL NOT NULL
)
""")

conn.commit()
conn.close()