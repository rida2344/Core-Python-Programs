#Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
# Function to calculate square
def square(num):
    return num * num  # or num ** 2

# Call the function and pass a number
num = float(input("Enter a number: "))

# Display the result
print(f"The square of {num} is: {square(num)}")

"""OUTPUT
Enter a number: 5
The square of 5.0 is: 25.0"""
