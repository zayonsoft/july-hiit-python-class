import sqlite3

with sqlite3.connect("testing.db") as conn:
    cursor = conn.cursor()

    sql = """SELECT * FROM students"""

    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        student_id = row[0]
        matric = row[1]
        first_name = row[2]
        last_name = row[3]

        print(f"""
ID: {student_id}
Matric Number: {matric}
First Name: {first_name}
Last Name: {last_name}
""")
        