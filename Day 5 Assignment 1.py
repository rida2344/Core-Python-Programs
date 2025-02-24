# Function to perform division
def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Call the function and pass two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the result
result = div(num1, num2)
print(f"The result of division is: {result}")

""" OUTPUT
Enter the first number: 9
Enter the second number: 3
The result of division is: 3.0 """
