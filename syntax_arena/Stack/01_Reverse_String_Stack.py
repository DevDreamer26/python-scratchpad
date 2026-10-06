#  Reverse a string using stack 

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    
    def is_empty(self):
        return len(self.items) == 0
    

def reverse_string(input_str):
    my_stack = Stack()
    
    
    for c in input_str:
        my_stack.push(c)
        
        
    reversed_str = ""
    while not my_stack.is_empty():
        reversed_str += my_stack.pop()
    return reversed_str



# Example usage : 
original = "Python"

output = reverse_string(original)

print(output)


