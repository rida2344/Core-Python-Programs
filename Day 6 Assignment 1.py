#Write a python program to reverse a number using a while loop.
# Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        rev = rev * 10 + digit  # Append the digit to reversed number
        num //= 10  # Remove the last digit
    return rev

# Input from user
num = int(input("Enter a number: "))

# Handle negative numbers
if num < 0:
    reversed_num = -reverse_number(-num)
else:
    reversed_num = reverse_number(num)

# Display result
print(f"Reversed number: {reversed_num}")
'''output
Enter a number: 234
Reversed number: 432'''
