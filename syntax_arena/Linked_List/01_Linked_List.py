class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Creating the nodes
a = Node(10)
b = Node(20)
c = Node(30)

# Linking them 
a.next = b
b.next = c

# Declaring head
head = a

# printing them together

current = head
while current is not None:
    print(current.data)
    current = current.next
    
