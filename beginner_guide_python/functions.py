# it is a simple file with function and also a module too
# import functions
# from functions import * - globallyenabled will be
# from functions import greet

def greet(namePerson, hotelName, hotelsStarsRate=4):
    print(f'Hello,{namePerson}, welcome to the hotel {hotelName} {hotelsStarsRate} stars')

greet('Andrii', 'Khreschatyk', 5)

greet(hotelName='California', namePerson='William')

