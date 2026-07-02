"""
Project: Fibonacci Series
Author: Mocherla Kasthuri
Description: Prints the Fibonacci series up to the specified number of terms.
"""

terms = int(input("Enter the number of terms: "))

a, b = 0, 1

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b
