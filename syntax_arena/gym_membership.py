month = int(input("Enter month : "))
def total_amount():
    if month == 1:
        print("2000")
    elif month == 3:
        print("5000")
    elif month == 6:
        print("9000")
    elif month == 9:
        print("12000")
    elif month == 12:
        print("15000")
    else:
        print("Choose between 1,3,6,9 and 12")
total_amount()

