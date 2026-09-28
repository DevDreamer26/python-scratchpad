# Given a string, write a function that returns a new string containing every second character, starting from the first character.

# Input
# text = "abcdefgh"
# Expected Output
# "aceg"
# More examples
# "Python"    → "Pto"
# "abcdef"    → "ace"
# "HelloWorld" → "Hlool"

def extract_alternate_characters(text):
    
    # return text[::2]
    result = ''
    for i in range(len(text)):
        if i%2==0:
            result += text[i]
            
    return result  
    
print(extract_alternate_characters("HelloWorld"))
