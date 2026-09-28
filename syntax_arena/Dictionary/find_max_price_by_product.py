# Question

# Given a list of product transactions where each sublist contains:

# [product_name, price]

# Some products appear multiple times with different prices.

# Write a function that creates a dictionary where:

# key → product name
# value → the highest price at which that product appears
# Input
# products = [
#     ['Laptop', 55000],
#     ['Phone', 30000],
#     ['Laptop', 62000],
#     ['Headphones', 5000],
#     ['Phone', 28000],
#     ['Laptop', 58000],
#     ['Headphones', 7000]
# ]
# Expected Output
# {
#     'Laptop': 62000,
#     'Phone': 30000,
#     'Headphones': 7000
# }

def find_max_price_by_product(products):
    output = {}

    for item in products:
        if item[0] in output:
            if item[1]>output[item[0]]:  # Comparing with the previous price
                output[item[0]] = item[1]
        else:
            output[item[0]] = item[1]
    return output
            
            
print(find_max_price_by_product([
    ['Laptop', 55000],
    ['Phone', 30000],
    ['Laptop', 62000],
    ['Headphones', 5000],
    ['Phone', 28000],
    ['Laptop', 58000],
    ['Headphones', 7000]
]))

