import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()

    rows = cursor.execute("""
SELECT * FROM users
        """)
    print(rows.fetchall())
