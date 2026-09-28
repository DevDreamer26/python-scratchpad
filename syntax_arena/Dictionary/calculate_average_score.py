# Given a list of exam records where each sublist contains:

# [student_name, score]

# A student can appear multiple times because they may have taken multiple exams.

# Write a function that returns a dictionary where:

# key → student's name
# value → their average score
# Input
# scores = [
#     ['Alice', 80],
#     ['Bob', 70],
#     ['Alice', 90],
#     ['Charlie', 60],
#     ['Bob', 85],
#     ['Alice', 70],
#     ['Charlie', 80]
# ]
# Expected Output
# {
#     'Alice': 80.0,
#     'Bob': 77.5,
#     'Charlie': 70.0
# }


def calculate_average(scores):
    data = {}

    for item in scores:
        name = item[0]
        score = item[1]

        if name in data:
            data[name][0] += score
            data[name][1] += 1
        else:
            data[name] = [score, 1]

    for name in data:
        data[name] = data[name][0] / data[name][1]

    return data


print(calculate_average([
    ['Alice', 80],
    ['Bob', 70],
    ['Alice', 90],
    ['Charlie', 60],
    ['Bob', 85],
    ['Alice', 70],
    ['Charlie', 80]
]))


# Trial ----> 
# def calculate_averagea_score(scores):
#     total ={}
#     occurace = {}
#     output ={}
    
#     for item in scores:
        
#         if item[0] in total:
           
#             occurace[item[0]] +=1
        
#             total[item[0]] = item[1]+total[item[0]]
            
#         else:
#             total[item[0]] = item[1]
#             occurace[item[0]] = 1
   
#         average_value = total[item[0]]/occurace[item[0]]
    
#         output[item[0]] = average_value
   
#     return output

# print(calculate_averagea_score([
#     ['Alice', 80],
#     ['Bob', 70],
#     ['Alice', 90],
#     ['Charlie', 60],
#     ['Bob', 85],
#     ['Alice', 70],
#     ['Charlie', 80]
# ]))








