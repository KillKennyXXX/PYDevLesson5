import json

money = 0
history = {}
def decorator(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 15)
        print(f(*args, **kwargs))
        # поведение после вызова
        print('*' * 15)
    # возвращается функция inner с новым поведением
    return inner

def history_back():
    try:
        with open('history.json', 'r') as f:
            result = json.load(f)
            return result
    except:
        return {}

def money_back():
    try:
        with open('money.json', 'r') as f:
            result = json.load(f)
            return int(result)
    except:
        return 0

def addMoney(money):
    try:
        sum = int(input('Введите сумму на сколько пополнить счет'))
    except ValueError:
        print('Необходимо ввести число')
    money += sum if sum > 0 else 0
    #print(money)

def purchase(money, history):
    try:
        sum = int(input('Введите сумму покупки'))
    except ValueError:
        print('Необходимо ввести число')
    if sum > 0 and sum <= money:
        money -= sum
        name = input('Введите название покупки')
        history[name] =sum
    else:
        print('Покупку произвести невозможно')

@decorator
def history_view(history):
    listA = []
    [listA.append(f'{key} --> {values}') for key, values in history.items()]
    return listA

def money_save(money):
    with open('money.json', 'w') as f:
        json.dump(money, f)
def history_save(history):
    with open('history.json', 'w') as f:
        json.dump(history, f)

    # print(money)

def view(money, history):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            addMoney(money)
        elif choice == '2':
            purchase(money, history)
        elif choice == '3':
            history_view(history)
        elif choice == '4':
            money_save(money)
            history_save(history)
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    money = money_back()
    history = history_back()
    view(money, history)
