def calculate_the_grade(score):
    if score < 0 or score > 100:
        return "error, please enter valid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score=float(input("enter your score between 0 to 100:"))

    grade=calculate_the_grade(score)
    print(f"Grade:{grade}")

except:
    print("enter a valid score")