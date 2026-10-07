import sys
import gc

class User:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        # This runs automatically the exact millisecond the object is destroyed from RAM
        print(f"💥 Memory Cleared: The User object for '{self.name}' has been deleted from RAM!")

# 1. We create the object. Reference count = 1
user1 = User("Alice") 

# 2. Let's see how many things point to it (sys.getrefcount adds 1 temporarily)
print(f"Current references: {sys.getrefcount(user1) - 1}")

# 3. We point a second variable to the SAME object. Reference count = 2
user2 = user1 
print(f"Current references after user2: {sys.getrefcount(user1) - 1}")

print("--- Setting user1 to None ---")
user1 = None  # Reference count drops to 1 (user2 still holds it)

print("--- Setting user2 to None (Count hits 0) ---")
user2 = None  # Reference count hits 0! Watch what happens next:

print("End of script.")
