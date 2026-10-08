numbers = [1,2,3,4,5]

squares = []

for num in numbers:
    squares.append(num**2)
    
print(squares)


squaresX = [num**2 for num in numbers]

print(squaresX)

print(squaresX==squares)
print(squaresX is squares)


