import sqlite3

print("Welcome to Class List Entering")
print("-----------------------------")
matric_number = input("Enter Your Matric Number: ")
first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")


with sqlite3.connect("my_class.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS
students(
    id INTEGER PRIMARY KEY,
    matric_number TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT
)
""")

    sql = """
    INSERT INTO students(matric_number, first_name, last_name) 
    VALUES (?, ?, ?)
    """
    cursor.execute(sql, (matric_number, first_name, last_name))
