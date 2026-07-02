"""
Project: To-Do List
Author: Mocherla Kasthuri
Description: A simple command-line to-do list that stores tasks in a text file.
"""

FILE_NAME = "tasks.txt"

def show_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("\nNo tasks found.")

def add_task():
    task = input("Enter a new task: ")
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
