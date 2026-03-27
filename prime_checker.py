# A simple script to check if a number is prime.
# Demonstrated skill: Logical loops and conditional handling.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 17 # You can change this number to test
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
