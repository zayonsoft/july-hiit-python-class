import sqlite3

with sqlite3.connect("testing.db") as conn:
    cursor = conn.cursor()
    sql = """
DELETE FROM students
WHERE id =? 
"""
    cursor.execute(sql, (2,))
