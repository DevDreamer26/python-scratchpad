enemies = 1

def increase_enemies():

    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()

print(f"Enemies outside function: {enemies}")

def greet_with(name, location):
    print(f"Hello {name}, how's it in like {location}")
    
greet_with("Bidyasagar","AEC")
