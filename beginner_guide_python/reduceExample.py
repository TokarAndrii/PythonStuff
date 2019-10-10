from functools import reduce
array = [ 1 , 3, 5, 6, 2 ] 

result = functools.reduce(lambda current, total: current + total, array)
print(result, ' - result')
