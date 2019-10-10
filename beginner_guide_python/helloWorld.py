# this is comment print('hello world!')
# to run python helloWorl.py
print('hello world!')

firstName = 'Andrii'
lastName = 'Tokar'
print(firstName, ' - firstName')
print(firstName + " " + lastName, '- fullName')
fullName = f'{firstName} {lastName} - fullName literal'
print(fullName)

otherWayFullName = '{0} {1} - fullName format'.format(
    firstName, lastName)

print(otherWayFullName)

a = 3
b = 4
c = '4'
d = 5
print(f'{a + b} = a + b')
print(f'{a ** b} = a ** b')
print(firstName + str(a))
print(int(c) + d)
print(float(c) + d)

myvar = 'myVar'
myvar2 = 5
myvar1 = myvar + myvar2
print(myvar1)
