number = int(input("Enter the number here = "))
# root = int(number**0.5)

def check_prime():
    if number<=0:
        print("Number must be positive integer.")
    elif number == 1:
        print(f"{number} is neither prime nor a composite number.")
    elif number == 2 or number == 3:
        print(f"{number} is a prime number.")
    elif number%2 == 0 or number%3 == 0:
        print(f"{number} is a composite number.")
    else:
        # Here i learnt this syntax for variable in range(start,stop,steps) and stop value is excluded
        # for i in range(5,root+1,6): 
        i = 5
        while i * i <= number:
            if number%i == 0 or number%(i+2) == 0:
                print(f"{number} is a composite number")
            i += 6
        print(f"{number} is a prime number.")
    
check_prime()

# More clean code ------>

def is_prime(n):
    if n <= 1:
        return "Enter a positive integer greater than 1"
    
    if n <= 3:
        return f"{n} is a prime number"
    
    if n % 2 == 0 or n % 3 == 0:
        return f"{n} is a composite number"
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return f"{n} is a composite number"
        i += 6
    
    return f"{n} is a prime number"


# Input
number = int(input("Enter the number = "))
print(is_prime(number))