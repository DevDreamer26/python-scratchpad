# Create a new list containing only the words that has exactly two 'a' characters.

strs = ["eat", "hello", "tea", "python", "bat", "amazon", "aahgv", "aaagbh", "aaaa", "mango"]

new_list = []

for word in strs:
    count = 0 
    for char in word:
        if char == "a":
            count += 1
    if count == 2:                 #Exactly 2 a we need 
        new_list.append(word)
    
print(new_list)

print(sorted("eat"))
