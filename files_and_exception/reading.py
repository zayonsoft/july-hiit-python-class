file_name = "files/person.txt"
with open(file_name, "r") as file:
    content = file.readlines()


print(content)  # returns a list
