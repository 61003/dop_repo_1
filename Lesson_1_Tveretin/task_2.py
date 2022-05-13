from os import listdir
from os.path import isfile


def print_directory_contents(dir):
    items = listdir(dir)
    for item in items:
        file = f'{dir}/{item}'
        if not isfile(file):
            print_directory_contents(file)
        else:
            print(file)


print_directory_contents('C:/Program Files/Notepad++')
