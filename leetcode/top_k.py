nums = [1,1,1,2,2,3]

k= 2

frequency = {}

for i in nums:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i]=1
        
sorted_frequency = sorted(frequency.items(), key = lambda pair: pair[1], reverse=True)

new_list = [item[0] for item in sorted_frequency[:k]] #list comprehension.

# for item in sorted_frequency[:k]:
#     new_list.append(item[0])

print(new_list)

# fn ={
#     1:3,
#     2:2,
#     3:1
# }
# print(fn.keys())
# print(fn.values())
# print(fn.items())


# new_dict = {
#     3:1,
#     1:3,
#     2:2
    
# }
# print(sorted(new_dict.items()))

