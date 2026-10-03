class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        # 1. Create the new node
        new_node = Node(new_data)
        
        # 2. Point new node's next to the current head
        new_node.next = self.head
        
        # 3. Move the head to point to the new node
        self.head = new_node
        
        
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current =current.next
        return " ".join(elements)
    
#Initialize the linked list
new_list = LinkedList()

 

a = Node(20)
b = Node(30)

a.next = b

new_list.head = a

# Insert at the beginning
new_list.insert_at_beginning(10)
new_list.insert_at_beginning(100)
new_list.insert_at_beginning(1000)

print(new_list.display())



