file_name = "files/person.txt"
with open(file_name, "r") as file:
    for text in file:
        print(text.strip())
