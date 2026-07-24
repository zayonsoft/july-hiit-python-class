my_table = {
    "color": "red",
    "owner": "HiiT",
    "no_of_legs": 4,
    "is_good": True,
}

print(my_table.get("color"))
print(my_table["color"])

# getting the owner

owner = my_table.get("owner")
print(f"Table Owner is: {owner}")

my_table["food"] = "Amala & Gbegiri"
my_table["color"] = "Green"
print(my_table)

print(my_table.get("food"))
