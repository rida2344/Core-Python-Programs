# Function to calculate factorial using while loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    fact = 1
    while n > 0:
        fact *= n  # Multiply fact by n
        n -= 1  # Decrease n by 1
    return fact

# Input from user
num = int(input("Enter a number: "))

# Display the result
print(f"Factorial of {num} is: {factorial(num)}")
'''OUTPUT
Enter a number: 3
Factorial of 3 is: 6'''
