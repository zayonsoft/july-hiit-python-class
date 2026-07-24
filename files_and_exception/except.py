file_name = "file/wrong_name.txt"

try:
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found")
