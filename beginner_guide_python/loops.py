peoples = ['firstMan', 'secondName', 'thirdName']

for people in peoples:
    print(f'{people} - people at for')


index = 0
while index < len(peoples):
    print(f'{peoples[index]} - people at while')
    index += 1
