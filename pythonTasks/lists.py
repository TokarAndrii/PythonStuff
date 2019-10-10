a = ['spam', 'eggs', 100, 1234]
print(a)

# Replace some items:
a[0:2] = [1, 12]
print(a)
# [1, 12, 100, 1234]

# Remove some:
a[0:2] = []
print(a)
# [100, 1234]

# Clear the list: replace all items with an empty list
a[:] = []
print(a)
# []

q = [2, 3]
p = [1, q, 4]
p[1].append('xtra')
print(p)
