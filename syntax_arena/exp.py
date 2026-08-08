k = 2
example_tuple_list = [
    (1, 3),
    (2, 2),
    (3, 1)
]
new_list = []
for item in example_tuple_list[:k]:
    new_list.append(item[0])
    
print(new_list)


