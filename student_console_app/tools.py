import sqlite3

DB_NAME = "record.db"


# this function must be called first to ensure that the databse has been created
def create_database():
    # Creating a database table
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        sql = """
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY,
        matric_number TEXT UNIQUE,
        email TEXT,
        first_name TEXT,
        last_name TEXT,
        department TEXT,
        age INTEGER
    )
    """
        cursor.execute(sql)
    # DATABASE TABLE CREATED


def add_new_record(matric_number, email, first_name, last_name, department, age):

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        sql = """
        INSERT INTO student(matric_number, email, first_name, last_name, department, age)
        VALUES (?,?,?,?,?,?)
        """
        try:
            cursor.execute(
                sql, (matric_number, email, first_name, last_name, department, age)
            )
            print("Student added successfully")
        except sqlite3.IntegrityError:
            print(f"Matric number '{matric_number}' already exists in the database")


def retrieve_students_record():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        sql = """SELECT * FROM student"""

        cursor.execute(sql)

        rows = cursor.fetchall()
        print("----------Student Information Record-----------")
        for row in rows:
            id = row[0]
            matric_number = row[1]
            email = row[2]
            first_name = row[3]
            last_name = row[4]
            department = row[5]
            age = row[6]

            info = f"""
    ID: {id}
    Matric Number: {matric_number}
    Email: {email}
    First Name: {first_name}
    Last Name: {last_name}
    Department:{department}
    Age: {age}
            """
            print(info)


def retrieve_one_record(matric_number):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Check if a student has the sent matric number
        sql = """SELECT * from student
            WHERE matric_number=?
            """
        cursor.execute(sql, (matric_number,))
        student = cursor.fetchone()

        if not student:
            print(f"Student with matric number '{matric_number}' not found")
            return False

        print("................Selected Students Info...............")

        id = student[0]
        matric_number = student[1]
        email = student[2]
        first_name = student[3]
        last_name = student[4]
        department = student[5]
        age = student[6]

        info = f"""
ID: {id}
Matric Number: {matric_number}
Email: {email}
First Name: {first_name}
Last Name: {last_name}
Department:{department}
Age: {age}\n
"""
        print(info)

        return True


def update_last_name(matric_number, value):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        sql = """
UPDATE student
SET last_name = ?
WHERE matric_number = ?
"""
        cursor.execute(sql, (value, matric_number))
        print("student last name updated")


def update_first_name(matric_number, value):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        sql = """
UPDATE student
SET first_name = ?
WHERE matric_number = ?
"""
        cursor.execute(sql, (value, matric_number))
        print("student first name updated")


def update_email(matric_number, value):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        sql = """
UPDATE student
SET email = ?
WHERE matric_number = ?
"""
        cursor.execute(sql, (value, matric_number))
        print("student email updated!")


def update_department(matric_number, value):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        sql = """
UPDATE student
SET department = ?
WHERE matric_number = ?
"""
        cursor.execute(sql, (value, matric_number))
        print("student department updated!")


def update_age(matric_number, value):
    if not value.isdigit():
        print("Age must be an integer")
        return
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        sql = """
        UPDATE student
        SET age = ?
        WHERE matric_number = ?
        """
        cursor.execute(sql, (value, matric_number))
        print("student age updated!")


def delete_existing_student(matric_number):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Check if a student has the sent matric number
        sql = """SELECT * from student
        WHERE matric_number=?
        """

        cursor.execute(sql, (matric_number,))
        student = cursor.fetchone()

        if student:
            sql = """
            DELETE FROM student
            WHERE matric_number=?
            """
            cursor.execute(sql, (matric_number,))

            print(f"Student with matric number '{matric_number}' deleted")

        else:
            print(f"Matric number doesn't exist")


def generate_students_txt():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        sql = """SELECT * FROM student"""

        cursor.execute(sql)

        rows = cursor.fetchall()
        student_file = "students_record.txt"
        with open(student_file, "w") as file:

            file.write("----------Student Information Record-----------\n")
            file.close()
            for row in rows:
                id = row[0]
                matric_number = row[1]
                email = row[2]
                first_name = row[3]
                last_name = row[4]
                department = row[5]
                age = row[6]

                info = f"""
ID: {id}
Matric Number: {matric_number}
Email: {email}
First Name: {first_name}
Last Name: {last_name}
Department:{department}
Age: {age}\n
                    """
                with open(student_file, "a") as file:
                    file.write(info)
            print(f"Student record written into {student_file}")
