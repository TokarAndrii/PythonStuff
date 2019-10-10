from functools import reduce
array = [1, 3, 5, 6, 2]


result = reduce(lambda current, total: current + total, array, 100)
print(result, ' - result')
