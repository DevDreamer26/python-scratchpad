# manual implementation of a singly linked list using nested dictionaries in Python

head = {"value":10,
        "next":{"value":20,
                "next":{"value":30,
                        "next":{"value":40,
                                "next":None}
                        }
                }
        }

"""
10 --> 20 --> 30 --> 40 --> None

"""

print(head["next"]["next"]["next"]["value"])


# Pythonic way of creating Linked List 

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
        
        
head = Node(10)
head.next =  Node(20)
head.next.next =  Node(30)
head.next.next.next =  Node(40)
head.next.next.next.next =  Node(50)
head.next.next.next.next.next =  None

print(head.next.next.next.next.value)

