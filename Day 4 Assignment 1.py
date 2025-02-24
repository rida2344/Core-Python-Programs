#Python program to check leap year  or not.
#TakeInput year from user
year = int(input("Enter a year: "))

#Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#output
#Enter a year: 2024
#2024 is a leap year.
