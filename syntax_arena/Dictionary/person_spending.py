
# transactions = [
#     ['Alice', 100],
#     ['Bob', 50],
#     ['Alice', 75],
#     ['Charlie', 120],
#     ['Bob', 30],
#     ['Charlie', 80],
#     ['Alice', 25]
# ]
def total(transactions):
    total_amount ={}
    
    for item in transactions:
        if item[0] in total_amount:
            total_amount[item[0]]= total_amount[item[0]] + item[1]
        else:
            total_amount[item[0]] = item[1]
            
    return total_amount
        

        
    

print(total( [['Alice', 100],
    ['Bob', 50],
    ['Alice', 75],
    ['Charlie', 120],
    ['Bob', 30],
    ['Charlie', 80],
    ['Alice', 25]]))