import console_manager as cm
import use_functions as bank
import victory
while True:
    cm.viewCurDir()
    print('1. - создать(файл/папку')
    print('2. - удалить (файл/папку)')
    print('3. - копировать (файл/папку)')
    print('4. - просмотр содержимого рабочей директории')
    print('5. - посмотреть только папки')
    print('6. - посмотреть только файлы')
    print('7. - просмотр информации об операционной системе')
    print('8. - создатель программы')
    print('9. - играть в викторину')
    print('10. - мой банковский счет')
    print('11. - смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        cm.addFD(cm.getInput())
    elif choice == '2':
        cm.dellFD(cm.getInput())
    elif choice == '3':
        cm.copyFD(cm.getInput())
    elif choice == '4':
        print(cm.view())
    elif choice == '5':
        print(cm.viewF())
    elif choice == '6':
        print(cm.viewD())
    elif choice == '7':
        print(cm.getOsInfo())
    elif choice == '8':
        print(cm.about())
    elif choice == '9':
        victory.game()
    elif choice == '10':
        bank.view(bank.money_back(), bank.history_back())
    elif choice == '11':
        cm.chDir_(cm.getInput())
    elif choice == '12':
        cm.quit()
        break
    else:
        print('Неверный пункт меню')