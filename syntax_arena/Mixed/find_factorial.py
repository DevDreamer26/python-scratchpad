# import sys

# sys.set_int_max_str_digits(0)  , this is for large input.


# Iterative approach


# num = int(input("Enter a number: "))

# factorial = 1

# if num<0:
#     print("Factorial does not exist for negative numbers.")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num+1):
#         factorial *=i
#     print(f"The factorial of {num} is {factorial}")
    
    
# Recursive Approach

def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n-1)
    
num = int(input("Enter a number : "))

if num <0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {find_factorial(num)}")