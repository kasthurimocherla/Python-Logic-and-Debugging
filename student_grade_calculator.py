"""
Project: Student Grade Calculator
Author: Mocherla Kasthuri
Description: Calculates total marks, percentage, and assigns a grade.
"""

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

print("=== Student Grade Calculator ===")

subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    total += mark

percentage = total / subjects
grade = calculate_grade(percentage)

print("\n===== Result =====")
print(f"Total Marks: {total:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
