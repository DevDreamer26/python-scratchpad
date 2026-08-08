# Without using any built-in methods like sorted() or count(), write a program that counts how many times the letter "a" appears in all the words combined.

strs = ["eat", "hello", "tea", "python", "bat", "amazon"]

count = 0

for word in strs:
    # print("Word:", word)
    for char in word:
        # print("Character:", i)
        if char == "a":
            count += 1
print(f"Number of letter 'a' appears in all the words combined is : {count}")
            
            
