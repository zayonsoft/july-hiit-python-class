every_body_in_class = ["Neymar", "Ronaldo", "Suarez", "Mbappe"]

first_person = every_body_in_class[0]

last_person = every_body_in_class[-1]
# print(last_person)


numbers = [3, 5, 7, 1, 4, 6, 8, 9, 10, 2]
numbers.sort()
# print(numbers)


# Sorting of names

names = [
    "Tinubu",
    "Zaria",
    "Yakubu",
    "Mohamad",
    "Dorcas",
    "Abubakar",
    "Balewa",
    "balewa",
]
names.sort()
# print(names)

# Adding to the list
names.append("Favour")
names.append("Ade")

# Checking the length
length_of_names = len(names)

# print(f"We now have {length_of_names} in the list")
# print(names)

# Removing from the list
names.remove("balewa")
# print(names)


cars = ["Toyota", "Korope", "Mecedez", "Lexus"]
cars.insert(1, "Tesla")
# print(cars)
cars.pop(2)
# print(cars)


names = ["Tinubi", "Zaria", "Yakubu", "Mohamad"]

print(names)

names[0] = "Tinubu"

print(names)

# TO count how many times an element occured
print(names.count("Tinubu"))


# to merge list into one
every_body_in_class.extend(cars)
print(every_body_in_class)
