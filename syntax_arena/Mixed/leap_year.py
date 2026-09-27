# To check if a year is a leap year or not, we can use the following code:

year = int(input("Enter the year : "))

if year<0:
    print("Invalid year !")
else:
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
        
# Using the calendar module # Import the calendar module
import calendar

# Prompt the user to enter a year and convert it to an integer
year = int(input("Enter a year: "))

# Use the calendar.isleap() function to check the year
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
