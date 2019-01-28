import os
import shutil

run = []

def cd():
    try:
        name = run[1]
        os.chdir(name)
        print("Вы в деректории {}".format(os.getcwd()))
    except IndexError:
        print("Каталог {} не существует".format(name))

def dir():
    current_dir = os.getcwd()
    dir_list = os.listdir(current_dir)
    for directory in list(dir_list):
        print(directory)

def mkdir():
    name = run[1]
    try:
        os.mkdir(name)
        print("Дирректория {} создана".format(name))
    except FileExistsError:
        print('Дирректория {} уже существует'.format(name))

def rmdir():
    name = run[1]
    try:
        os.rmdir(name)
        print("Дирректория {} удалена".format(name))
    except FileNotFoundError:
        print('Дирректория {} не существует'.format(name))
