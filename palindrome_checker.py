"""
Project: Palindrome Checker
Author: Mocherla Kasthuri
Description: Checks whether the entered word or number is a palindrome.
"""

text = input("Enter a word or number: ")

if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
