try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    add = a + b + c
    print(f"{a} + {b} + {c} = {add}")


except ValueError:
    print("User entered something wrong")


# number = "12"
# print(number.isdecimal())
