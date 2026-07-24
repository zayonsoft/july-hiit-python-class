class Student:
    matric_number = "19040597"
    first_name = "Mohammad"
    last_name = "Tinubu"


student_1 = Student()
student_1.matric_number = "changed matric number"
student_1.first_name = "Adamu"
student_1.last_name = "Adamu"
print(student_1.matric_number)
print(student_1.first_name)
print(student_1.last_name)

student_2 = Student()
print(student_2.matric_number)
print(student_2.first_name)
print(student_2.last_name)
