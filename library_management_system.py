"""
Project: Library Management System
Author: Mocherla Kasthuri
Description: A simple library system to add, view, issue, and return books.
"""

library = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if not library:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(library, start=1):
                print(f"{i}. {book}")

    elif choice == "3":
        book = input("Enter book name to issue: ")
        if book in library:
            library.remove(book)
            print("Book issued successfully!")
        else:
            print("Book not available.")

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.append(book)
        print("Book returned successfully!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
