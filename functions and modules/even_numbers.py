# printing even numbers from 1 -100
print("-----------------------")
print("Even Numbers")
for even in range(2, 101, 2):
    print(even)

# printing odd numbers from 1 -100
print("-----------------------")
print("Odd Numbers")
for odd in range(1, 101, 2):
    print(odd)


def print_even_numbers(stop):
    for i in range(2, stop + 1, 2):
        print(i)


number_to_print = int(
    input("Enter a number and I'll print the even numbers from 1 till the number: ")
)
print_even_numbers(number_to_print)
