"""
Project: Expense Tracker
Author: Mocherla Kasthuri
Description: A simple expense tracker that stores expenses and calculates the total.
"""

expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Expense Name: ")
        amount = float(input("Amount: ₹"))
        expenses.append((item, amount))
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")
            for item, amount in expenses:
                print(f"{item} - ₹{amount:.2f}")

    elif choice == "3":
        total = sum(amount for _, amount in expenses)
        print(f"\nTotal Expenses: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
