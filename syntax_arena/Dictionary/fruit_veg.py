# Count Occurances

def count_occurances(items):
    
    item_count = {}

    for item in items:
        if item[1] in item_count:
            item_count[item[1]] +=1
        else:
            item_count[item[1]] = 1
            
    return item_count

print(count_occurances( [
    ['apple', 'fruit'],
    ['carrot', 'vegetable'],
    ['banana', 'fruit'],
    ['spinach', 'vegetable'],
    ['apple', 'fruit'],
    ['banana', 'fruit'],
    ['carrot', 'vegetable']
]))
        
