# Given a string containing words separated by spaces, reverse the order of the words, but keep each word itself unchanged.

# Examples
# Input:  "I love Python"
# Output: "Python love I"

# Input:  "Hello World"
# Output: "World Hello"

# Input:  "Python is awesome"
# Output: "awesome is Python"

def reverse_word(words):
    
    # "seperate".join(iterable) and .split() syntax -----> string.split(seperator,maxsplit)
    items =  words.split()
    
    return " ".join(items[::-1])
    
print(reverse_word('Python is awesome'))


#  Let's try using loop 
def reverse_word(words):
    items = words.split()
    result = ""

    for i in range(len(items) - 1, -1, -1):
        result += items[i] + " "

    return result.strip() # strip to remove the extra space at the end

# Important distinction

# .strip() removes whitespace from both ends:

# "  Hello World  ".strip()
# # "Hello World"

# It does not remove spaces between words


print(reverse_word("Python is awesome"))