# https: // docs.python.org/3.0/tutorial/controlflow.html

# for
a = ['cat', 'window', 'defenestrate']

for current in a:
    print(current, len(current))

for curr in a[:]:  # make a slice copy of the entire list
    if len(curr) > 6:
        a.insert(0, curr)

print(a)
# ['defenestrate', 'cat', 'window', 'defenestrate']

b = [*a]
print(b)
# ['defenestrate', 'cat', 'window', 'defenestrate']
