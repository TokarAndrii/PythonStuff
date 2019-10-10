# common in frameworks
# add additionals functionality to code
# https://www.datacamp.com/community/tutorials/decorators-python


def loggerUpper(func):
    def  wrapper(*args,**kwargs):
        print('logging execution...')
        bool(args) and print('The positional arguments are', args)
        bool(kwargs) and print('The keyword arguments are', kwargs)
        func(*args)
        print('logging done...')
    return wrapper


@loggerUpper    
def someFunction(name, secondName):
    print(name, ' - name')


someFunction('Andrii', 'Tokar',)
