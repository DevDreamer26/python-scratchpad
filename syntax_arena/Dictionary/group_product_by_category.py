# Given a list of products where each sublist contains:

# [product_name, category]

# Write a function that groups the product names by their category.

# The function should return a dictionary where:

# key → category
# value → list of product names belonging to that category
# Input
# products = [
#     ['iPhone', 'Electronics'],
#     ['Shirt', 'Clothing'],
#     ['MacBook', 'Electronics'],
#     ['Jeans', 'Clothing'],
#     ['Headphones', 'Electronics'],
#     ['Shoes', 'Footwear'],
#     ['Jacket', 'Clothing'],
#     ['Socks', 'Footwear']
# ]
# Expected Output
# {
#     'Electronics': ['iPhone', 'MacBook', 'Headphones'],
#     'Clothing': ['Shirt', 'Jeans', 'Jacket'],
#     'Footwear': ['Shoes', 'Socks']
# }


def group_products_by_category(products):
    output = {}

    for item in products:
        if item[1] in output:
            output[item[1]].append(item[0])
            
        else:
            output[item[1]] = [item[0]] # Make list . basically u have to convert, 
            
    return output

print(group_products_by_category([
    ['iPhone', 'Electronics'],
    ['Shirt', 'Clothing'],
    ['MacBook', 'Electronics'],
    ['Jeans', 'Clothing'],
    ['Headphones', 'Electronics'],
    ['Shoes', 'Footwear'],
    ['Jacket', 'Clothing'],
    ['Socks', 'Footwear']
]))

