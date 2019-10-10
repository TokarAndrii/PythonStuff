# https://gist.github.com/revolunet/537a3448cff850231a74
# https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them/

# Использование * и ** для передачи аргументов в функцию;
# Использование * и ** для сбора переданных в функцию аргументов;
# Использование ** для принятия только именованные аргументов;
# Использование * при распаковке кортежей;
# Использование * для распаковки итерируемых объектов в список/кортеж;
# Использование ** для распаковки словарей в другие словари.

# destructuring
myList = [1, 2, 3, 4, ]
first, second, *_ = myList

print(first)
print(second)
print(*_)

# spread
newList = [0, 0, *myList]
print(newList)


date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}

filename = {
    **date_info,
    **track_info,
    'group': "Python Meetup"
}
print(filename)
# output {'year': '2020', 'month': '01', 'day': '01', 'artist': 'Beethoven', 'title': 'Symphony No 5', 'group': 'Python Meetup'}

def logger(first, *args):
    print(f'{first} - first')
    print(list(map(lambda curr: curr + curr, args)), ' - newList') 

    
logger('a',1, 2)  
logger('a',1, 2, 3)

def loggerDictionary(first, **args):
    print(f'{first} - first')
    print(f'{args}- args')
    print(list(map(lambda curr: curr + curr, args)), ' - newList') 

    
loggerDictionary('a',name="name", age=2)  

