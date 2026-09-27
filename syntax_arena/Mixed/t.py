strs = ["eat", "hello", "tea", "python", "bat"]

# return the words that starts with "t"

word_starts_with_t = []

for word in strs:
    if len(word)>0 and  word[0] == "t":
        word_starts_with_t.append(word)
        
print(word_starts_with_t)



