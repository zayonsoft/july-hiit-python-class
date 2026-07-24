class Student:
    def __init__(self, matric_no, first_name, last_name):
        self.matric_no = matric_no
        self.first_name = first_name
        self.last_name = last_name


tin = Student("1905", "Tinbzy", "Asiwajs")
tin_two = Student("190574", "Tin", "Asiws")
print(f"Tin1's Matric Number: {tin.matric_no}")
print(f"Tin2's Matric Number: {tin_two.matric_no}")
