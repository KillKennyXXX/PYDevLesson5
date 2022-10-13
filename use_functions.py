
money = 0
history = {}
def shop():

    def addMoney():
        global money
        try:
            sum = int(input('Введите сумму на сколько пополнить счет'))
        except ValueError:
            print('Необходимо ввести число')
        money += sum if sum > 0 else 0
        #print(money)

    def purchase():
        global money
        global history
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


    def history():
        global history
        for key, values in history.items():
            print(f'{key} --> {values}')

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            addMoney()
        elif choice == '2':
            purchase()
        elif choice == '3':
            history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

