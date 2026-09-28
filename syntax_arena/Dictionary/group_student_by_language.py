# Given a list of students where each sublist contains:

# [student_name, programming_language]

# write a function that groups the students based on the programming language they chose.

# The function should return a dictionary where:

# The key is the programming language.
# The value is a list containing the names of all students who chose that language.
# Input
# students = [
#     ['Alice', 'Python'],
#     ['Bob', 'Java'],
#     ['Charlie', 'Python'],
#     ['David', 'C++'],
#     ['Eve', 'Python'],
#     ['Frank', 'Java'],
#     ['Grace', 'C++']
# ]
# Expected Output
# {
#     'Python': ['Alice', 'Charlie', 'Eve'],
#     'Java': ['Bob', 'Frank'],
#     'C++': ['David', 'Grace']
# }

def group_students_by_language(students):
    #create the dictionary
    output = {} 

    for item in students:
        if item[1] in output:
            output[item[1]].append(item[0])
        else:
            output[item[1]] = [item[0]]
            
    return output

print(group_students_by_language([
    ['Alice', 'Python'],
     ['Bob', 'Java'],     ['Charlie', 'Python'],
    ['David', 'C++'],
    ['Eve', 'Python'],
    ['Frank', 'Java'],
    ['Grace', 'C++']
 ]))