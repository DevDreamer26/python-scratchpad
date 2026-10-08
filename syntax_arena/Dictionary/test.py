from functools import reduce

nums = [3,2,6,8,4,9]

even_nums = list(filter(lambda n : n%2==0,nums))

print(even_nums)

doubles = list(map(lambda n: n*2,even_nums))

print(doubles)

sum_all = reduce(lambda n,m:n+m, doubles)

print(sum_all)