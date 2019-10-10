# sort() — A method that modifies the list in-place
# sorted() — A built-in function that builds a new sorted list from an iterable

student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
]

# sort by age
#key parameter to specify a function to be called on each list element
print(sorted(student_tuples, key=lambda student: student[2]), 'student_tuples sorted')  
#output: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

print(sorted(student_tuples, key=lambda student: student[2], reverse=True), 'student_tuples sorted - reverse=True')  
#output: [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

print(student_tuples, ' - student_tuples after sorting')
# output [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

myList = [21, 3, 5, 7, 9, 11, 8, 2]

mappedMyList = list(map(lambda current:current + 1, myList)) 
print(f'{mappedMyList} - mappedMyList')
print(f'{myList} - myList')

list_a = [1, 2, 3]
list_b = [10, 20, 30]
print(list_b[0:2], ' - list_b[0:2]')

# Multiple Iterables to the Map Function
print(list(map(lambda x, y: x + y, list_a, list_b))) 
# Output: [11, 22, 33]

print(list(map(lambda x, y: y - x, list_a, list_b))) 
# Output: [11, 22, 33]

# filter
listBeforeFilter = [1, 2, 3, 4, 5, 6]
listAfterFilter = list(filter(lambda x : x % 2 == 0, listBeforeFilter))
print(listAfterFilter, ' - listAfterFilter')
# Output: [2, 4, 6]
