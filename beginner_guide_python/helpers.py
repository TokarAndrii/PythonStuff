from colorama import init, Fore

def printWithColor(message, isWarning=False):
    if isWarning:
        print(Fore.RED + message)
    else: 
        print(Fore.BLUE + message)
