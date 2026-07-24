number = int(input("Enter a number and I'll count to it: "))

for ii in range(1, number + 1):
    print(ii)
print("----------------------")
print("using while loop")
print("----------------------")

counter = 1
while counter <= number:
    print(counter)
    counter = counter + 1
