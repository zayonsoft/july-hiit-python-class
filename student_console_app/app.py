"""
Task: Developing a Console Application
-Write a Python Program that collects student information like,
Matric number:
Email:
Department:
Age:
etc.

Stores the information using SQLite database.
The user of the application should be able decide whether they want to create new student record, retrieve existing student record, update a certain record or delete it (CRUD).
Additional note (still thinking about it): Might add that they should be able export the info into a txt file and it should contain all student info.
"""

from tools import (
    create_database,
    add_new_record,
    add_new_record,
    generate_students_txt,
    delete_existing_student,
    retrieve_students_record,
    update_age,
    update_department,
    update_email,
    update_first_name,
    update_last_name,
    retrieve_one_record,
)


def main():
    # Create the database if it doesn't exist
    create_database()

    options = """
Welcome to Student Record App
Enter:
1 - Add new student record
2 - Retrieve Student Data
3 - Update Existing Record
4 - Delete Existing record
5 - Export record as txt
6 - exit
"""

    REPEAT = True

    while REPEAT:
        # promt the user for an input
        print(options)
        response = input("> ")

        if response == "1":
            # adding new student
            print("-------------Adding new student record-------------")
            matric_no = input("Enter Your Matric Number: ")
            email = input("Enter Your Email: ")
            first_name = input("Enter Your First Name: ")
            last_name = input("Enter Your Last Name: ")
            department = input("Department: ")
            age = input("Enter Your age: ")
            if not age.isdigit():
                print("Error: Age must be a number (integer)")
                return  # to stop execution of the main function

            add_new_record(matric_no, email, first_name, last_name, department, age)
        elif response == "2":
            retrieve_students_record()

        elif response == "3":
            # update existing record
            print("Update Existing record")
            message = """
    Enter:
    1 - to update email
    2 - to update department
    3 - to update first name
    4 - to update last name
    5 - to update age
    *To exit -> Enter any other key
    """
            print(message)
            response = input("Enter response: ")
            valid_responses = ["1", "2", "3", "4", "5"]
            if response not in valid_responses:
                print("exiting....")
                return

            matric_no = input("Enter Student Matric number: ")

            # The function will return true or false depending on whether the matric number exists or not
            if not retrieve_one_record(matric_no):
                return

            if response == "1":
                new_value = input("Enter Updated Email: ")
                update_email(matric_no, new_value)
            elif response == "2":
                new_value = input("Enter Updated Department: ")
                update_department(matric_no, new_value)
            elif response == "3":
                new_value = input("Enter Updated First Name: ")
                update_first_name(matric_no, new_value)
            elif response == "4":
                new_value = input("Enter Updated Last Name: ")
                update_last_name(matric_no, new_value)
            elif response == "5":
                new_value = input("Enter Updated Age: ")
                update_age(matric_no, new_value)

        elif response == "4":
            # delete existing record..
            matric_no = input("Enter Student Matric number: ")
            delete_existing_student(matric_no)

        elif response == "5":
            print("Exporting as txt...")
            generate_students_txt()

        else:
            print("exiting...........")
            return

        print("Do you want to perform another action?\n")
        question = input("1 - Yes (Continue)  2 - No: ")

        if question == "1":
            print("Okay, Continue enjoying the app")
            print("------------------------")
            # for Space
            print("")

        else:
            print("Thank you for using the app")
            print("Exiting....")
            REPEAT = False


if __name__ == "__main__":
    main()
