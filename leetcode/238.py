
#Brute-force solution
nums = [1,2,3,4,5]

output = []
for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
        if i != j:
            product *= nums[j]  
    output.append(product)
    
print(output)
