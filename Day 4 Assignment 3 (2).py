# Input a number from the user
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")
'''example output
Enter a number: 15
15.0 is a positive number.

Enter a number: -8
-8.0 is a negative number.

Enter a number: 0
The number is zero.'''
