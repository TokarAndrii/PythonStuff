for i in range(5, 10):
    print(i)
# 5
# 6
# 7
# 8
# 9

for i in range(0, 20, 5):
    print(i)
# 0
# 5
# 10
# 15


for i in range(-10, -100, -30):
    print(i)
# -10
# -40
# -70

print(range(10))
# range(0, 10)

print(list(range(5)))
# [0, 1, 2, 3, 4]

myList = ['Mary', 'had', 'a', 'little', 'lamb']
for curr in range(len(myList)):
    print(curr, myList[curr])
