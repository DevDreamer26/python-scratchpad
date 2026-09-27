def find_longest_word(words):
    
    if not words:
        return ""

    # return max(words,key=len)

    longest =""

    for c in words:
        if len(c)> len(longest):
            longest = c
    return longest
    
print(find_longest_word(["PHP", "Exercises", "Backend", "Python","supercalifragilisticexpialidocious"])) 