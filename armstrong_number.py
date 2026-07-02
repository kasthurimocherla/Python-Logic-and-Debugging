"""
Project: Armstrong Number Checker
Author: Mocherla Kasthuri
Description: Checks whether a given number is an Armstrong number.
"""

num = int(input("Enter a number: "))

order = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** order
    temp //= 10

if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
