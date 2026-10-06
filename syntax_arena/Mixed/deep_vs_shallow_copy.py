import copy

original = [1,2,[3,4]]

shallow_copy = copy.copy(original)
deep_copied = copy.deepcopy(original)



shallow_copy[2][0] ="X"
deep_copied[2][0] ="Y"


print(original)
print(shallow_copy)
print(original)
print(deep_copied)