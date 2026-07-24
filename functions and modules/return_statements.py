def returnSomething():
    return 2 + 24


# value = returnSomething()

# print(returnSomething())
# print(value)


def add_three_numbers(a, b, c):
    return a + b + c


def add_four_numbers(a, b, c, d):
    add = a + b + c + d
    return add


value = add_three_numbers(23, 64, 77)
# print(f"The sum is: {value}")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

the_sum = add_three_numbers(num1, num2, num3)
print(f"The sum is: {the_sum}")
print(f"The sum is: {add_three_numbers(num1, num2, num3)}")
