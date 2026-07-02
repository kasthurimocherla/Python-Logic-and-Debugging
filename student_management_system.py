"""
Project: Student Management System
Author: Mocherla Kasthuri
Description: A menu-driven application to manage student records.
"""

students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("✅ Student added successfully!")


def view_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\n===== Student Records =====")

    for student in students:
        print(f"ID    : {student['id']}")
        print(f"Name  : {student['name']}")
        print(f"Marks : {student['marks']}")
        print("-" * 30)


def search_student():
    search_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("\n===== Student Found =====")
            print(f"ID    : {student['id']}")
            print(f"Name  : {student['name']}")
            print(f"Marks : {student['marks']}")
            return

    print("❌ Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            new_marks = float(input("Enter New Marks: "))
            student["marks"] = new_marks
            print("✅ Student marks updated successfully!")
            return

    print("❌ Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("✅ Student deleted successfully!")
            return

    print("❌ Student not found.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
