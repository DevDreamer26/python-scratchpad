# Given a string, write a function that removes the first and last characters and returns the remaining string.

# Input
# text = "Python"
# Expected Output
# "ytho"
# Examples
# "Hello"   → "ell"
# "Python"  → "ytho"
# "abcdef"  → "bcde"

def remove_first_last(text):
    return text[1:-1]
    # [start:stop:step]
       
print(remove_first_last('Hello'))

