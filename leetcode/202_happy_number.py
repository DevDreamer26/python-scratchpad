
def isHappy_Number(num:int) -> bool:
    
    result = set()
    
    current_num = num
    
    
    while current_num != 1 and current_num not in result:
        
        result.add(current_num)
        total = 0
        for digit in str(current_num):
            n = int(digit)
            total += (n*n)
        
        
        current_num = total
        
    return current_num == 1
        
print(isHappy_Number(7))



