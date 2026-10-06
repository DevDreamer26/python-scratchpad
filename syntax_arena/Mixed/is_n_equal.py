a = [1,2,3,4,5]

b = [1,2,3,4,5]

c = b

print(a==b)  # Output True, comparing value


print(a is b) # Output False, They are stored in different places in memory.

# assigning  a new reference to the same object
print( c is b ) #Output --> true

