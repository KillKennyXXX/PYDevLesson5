from math import pi, sqrt, pow, hypot
import console_manager as cm
def test_filter():
    assert list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) == [2, 4, 6]
    assert list(filter(lambda x: x % 3 == 0 or x == 1, [1, 2, 3, 4, 5, 6]) )== [1, 3, 6]
    assert list(filter(lambda x: 'f' in x, ['fx', 'xxx', 'of','rr'])) == ['fx', 'of']
def test_map():
    assert list(map(lambda x: x, [1, 2, 3, 4, 5, 6])) == [1, 2, 3, 4, 5, 6]
    assert list(map(lambda x: x + 1, [1, 2, 3, 4, 5, 6])) == [2, 3, 4, 5, 6, 7]
    assert list(map(lambda x: x ** 2, [1, 2, 3])) ==[1, 4, 9]
def test_sorted():
    assert list(sorted([3, 2, 3, 4, 5, 1])) == [1, 2, 3, 3, 4, 5]
    assert list(sorted([3, 2, 3, 4, 5, 1], reverse=True)) == [5, 4, 3, 3, 2, 1]
def test_math():
    assert pi == 3.141592653589793
    assert sqrt(2) == 1.4142135623730951
    assert sqrt(1) == 1
    assert pow(2, 3) == 8.0
    assert pow(1, 3) == 1.0
    assert pow(3, 3) == 27.0
    assert hypot(2, 4) == 4.47213595499958
    assert hypot(3, 4) == 5.0
    assert hypot(-2, 3) == 3.6055512754639896
def test_console_manager():
    assert cm.viewF() == ['console_manager.py', 'main.py', 'test_python.py', 'use_functions.py', 'victory.py']
    assert cm.viewD() == ['.git', '.idea', '.pytest_cache', 'venv', '__pycache__']
    assert cm.view() == ['.git', '.idea', '.pytest_cache',  'console_manager.py', 'main.py', 'test_python.py', 'use_functions.py', 'venv', 'victory.py', '__pycache__']
    assert cm.about() == 'Создатель программы Шалыгин Алексей'
    assert cm.getOsInfo() == ('My OS is', 'win32', '(', 'nt', ')')

def test_mkdir():
    """Тест для функции с побочным эффектом"""
    cm.addFD('folder_mk')
    # папка есть на диске
    assert 'folder_mk' in cm.view()
    cm.copyFD('folder_mk')
    assert 'copy_folder_mk' in cm.view()
    cm.dellFD('folder_mk')
    assert 'folder_mk' not in cm.view()
    cm.dellFD('copy_folder_mk')
    assert 'copy_folder_mk' not in cm.view()
