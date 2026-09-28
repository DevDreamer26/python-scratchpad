# Given a list of lists, create a dictionary which keys are the first elements of every sublist and it's values are the sum of the integers of the second elements of every sublist.

# input: data = [['item1', 4], ['item2', 5], ['item3', 2], ['item2', 10], ['item3', 3], ['item1', 7]]

# output: {'item1': 11, 'item2': 15, 'item3': 5}

data = [['item1', 4], ['item2', 5], ['item3', 2], ['item2', 10], ['item3', 3], ['item1', 7]]

item_dict = {}

for item in data:
     
    if item[0] in item_dict:
        
       item_dict[item[0]] = item_dict[item[0]] + item[1]
    else:
        item_dict[item[0]] = item[1]
    
print(item_dict)

