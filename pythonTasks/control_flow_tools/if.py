# https: // docs.python.org/3.0/tutorial/controlflow.html


# if, elif, else
x = int(input('enter an integer: '))
print(x, ' - you entered')

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
