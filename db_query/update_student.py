import sqlite3

with sqlite3.connect("testing.db") as conn:
    cursor = conn.cursor()
    sql = """
UPDATE students
SET first_name=?, last_name=?
WHERE id=?
"""
    cursor.execute(sql, ("Pelumi", "PelumiLast Name", 2))
