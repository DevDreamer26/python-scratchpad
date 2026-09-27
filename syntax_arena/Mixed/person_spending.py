
transactions = [
    ['Alice', 100],
    ['Bob', 50],
    ['Alice', 75],
    ['Charlie', 120],
    ['Bob', 30],
    ['Charlie', 80],
    ['Alice', 25]
]

total_amount ={}

for person in transactions:
    if person[0] in total_amount:
        total_amount[person[0]]= total_amount[person[0]] + person[1] 
    else:
        total_amount[person[0]] = person[1]
        
print(total_amount)

