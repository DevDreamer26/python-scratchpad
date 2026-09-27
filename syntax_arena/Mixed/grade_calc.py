marks = int(input("Enter the marks obtained = "))

if marks<0 or marks>100:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
else:
    if marks>90:
        print("Grade obtained: A")
    elif marks>80 and marks<=90:
        print("Grade obtained: B")
    elif marks>70 and marks<=80:
        print("Grade obtained: C")
    elif marks>60 and marks<=70:
        print("Grade obtained: D")
    elif marks>50 and marks<=60:
        print("Grade obtained: E")
    else:        print("Grade obtained: F")
    

# here i learned how to use if-else statements to determine the grade based on the marks entered by the user. I also included a check for invalid marks to ensure that the input is within the acceptable range.
#use of logical operators (and) to combine conditions for grade determination. and or statements can be used to create more complex conditions for decision-making in the code.
