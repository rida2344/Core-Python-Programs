# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number using if-elif-else
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

# Display the largest number
print(f"The largest number is: {largest}")

#output
#Enter the first number: 2
#Enter the second number: 3
#Enter the third number: 4
#The largest number is: 4.0
