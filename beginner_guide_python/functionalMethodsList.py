from functools import reduce

list_b = [10, 20, 30]

res = reduce(lambda prev, curr: prev + curr, list_b)
print(f'{res} - res')
