import sqlite3

conn = sqlite3.connect("testing.db")

cursor = conn.cursor()

# creating the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS 
    students(
    id INTEGER PRIMARY KEY,
    matric_number TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT
    )
""")

# putting values into the table

query = """
INSERT INTO students(matric_number, first_name, last_name)
    VALUES (?, ?, ?)
"""
cursor.execute(query, (19064040, "AdeQudud", "Qudud"))
cursor.execute(query, (19064041, "another Student", "Student Last name"))


conn.commit()
cursor.close()
conn.close()
