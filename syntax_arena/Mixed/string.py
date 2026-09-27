strs = ["eat", "hello", "tea", "python", "bat"]

three_letter_words = []

for word in strs:
    if len(word) == 3:
        three_letter_words.append(word)

print(three_letter_words)