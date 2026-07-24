first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

file_name = f"files/person.txt"
with open(file_name, "w") as file:
    file.write(f"First Name: {first_name}\n")
    file.write(f"Last Name: {last_name}\n")
    file.write(f"Age: {age}\n")
