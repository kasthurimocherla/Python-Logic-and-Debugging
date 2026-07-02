text = input("Enter a word or number: ")

if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
