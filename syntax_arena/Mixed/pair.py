people = [
    ("Rahul", 25),
    ("Amit", 19),
    ("Zoya", 30)
]

sorted_people = sorted(people, key=lambda pair: pair[1], reverse=True)

print(sorted_people)
