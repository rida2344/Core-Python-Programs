def is_palindrome_number(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10  # Extract and append last digit
        num //= 10  # Remove last digit
    return original == rev

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if num >= 0 and is_palindrome_number(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

''' OUTPUT
Enter a number: 121
121 is a palindrome.'''
