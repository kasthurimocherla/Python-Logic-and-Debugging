"""
Project: Contact Book
Author: Mocherla Kasthuri
Description: A simple contact book to save and view contacts.
"""

contacts = {}

while True:
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        if contacts:
            print("\nSaved Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
