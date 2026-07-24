condition = True

while condition:
    a = int(input("Enter a Number"))
    b = int(input("Enter another Number"))

    add = a + b
    print(f"{a} + {b} = {add}")

    print("--------------------")
    print("Do you still want to  calculate? ")
    print("--------------------")

    response = input("To continue enter 'yes': ")

    if response.lower() == "yes":
        condition = True
    else:
        condition = False
