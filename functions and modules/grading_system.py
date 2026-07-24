def get_grade(score):
    if score >= 70 and score <= 100:
        return "A"
    elif score >= 60 and score <= 69:
        return "B"

    elif score >= 50 and score <= 59:
        return "C"

    elif score >= 45 and score <= 49:
        return "D"

    elif score >= 40 and score <= 44:
        return "E"

    elif score >= 0 and score <= 39:
        return "F"

    else:
        return "Invalid Score"


my_score = int(input("Enter your score: "))
grade = get_grade(my_score)
print(f"Grade: {grade}")
