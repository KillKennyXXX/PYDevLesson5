
import os
import shutil
import sys

# путь до текущей папки
def viewCurDir():
    print(f'Текущий путь: {os.getcwd()}')
def getInput ():
    return input("Введите название: ")
def addFD (name):
    if not os.path.exists(f'{name}'):
        if name.find('.') != -1:
            f = open(name, "w")
            f.close()
        else:
            os.mkdir(name)
def dellFD (name):
    if os.path.exists(f'{name}'):
        if os.path.isfile(os.path.join(os.getcwd(), name)):
            os.remove(name)
        else:
            os.rmdir(name)
def copyFD (name):
    if os.path.exists(f'{name}'):
        if name.find('.') != -1:
            shutil.copy(name, f'copy_{name}')
        else:
            shutil.copytree(name, f'copy_{name}')
def view():
    print(os.listdir())
def viewD():
    print(list(filter(lambda s: os.path.isdir(s), os.listdir())))
def viewF():
    print(list(filter(lambda s: os.path.isfile(s), os.listdir())))
def chDir_(name):
    os.chdir(name)
def getOsInfo():
    print('My OS is', sys.platform, '(', os.name, ')')
def about():
    print('Создатель программы Шалыгин Алексей')

