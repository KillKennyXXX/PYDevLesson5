
import os
import shutil
import sys

# путь до текущей папки
def viewCurDir():
    return f'Текущий путь: {os.getcwd()}'
def getInput ():
    return input("Введите название: ")
def addFD (name):
    if not os.path.exists(f'{name}'):
        open(name, "w").close() if name.find('.') != -1 else os.mkdir(name)
def dellFD (name):
    if os.path.exists(f'{name}'):
        os.remove(name) if os.path.isfile(os.path.join(os.getcwd(), name)) else os.rmdir(name)
def copyFD (name):
    if os.path.exists(f'{name}'):
        shutil.copy(name, f'copy_{name}') if name.find('.') != -1 else shutil.copytree(name, f'copy_{name}')
def view():
    return os.listdir()

def viewD():
    return list(map(lambda x: x +' ', filter(lambda s: os.path.isdir(s), os.listdir())))
def viewF():
    return list(map(lambda x: x +' ', filter(lambda s: os.path.isfile(s), os.listdir())))
def chDir_(name):
    os.chdir(name)
def getOsInfo():
    return 'My OS is', sys.platform, '(', os.name, ')'
def about():
    return 'Создатель программы Шалыгин Алексей'
def quit():
    with open('listdir.txt', 'w') as f:
        f.write('files:\n')
        f.writelines(viewF())
        f.write('\ndirs:\n')
        f.writelines(viewD())
