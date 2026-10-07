def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1
        
        
        
# Creating the generator object
counter = count_up_to(5)

for number in counter:
    print(number)
    
    
    
    