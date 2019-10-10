from array import array

#list collections of items
names = ['Andrii', "Blona"]
print(names[0])
names.insert(1,'Clisa',) #insert before index
print(names)
names.sort()
print(sorted(names))
print(names)

# array of digits
scores = array('d')
scores.append(98)
scores.append(100)
print(scores[0])
print(len(scores), ' - scores length')

#Arrays for: 
# - simple types
# - must all be the same type


#Lists for: 
# - store anything
# - store type
