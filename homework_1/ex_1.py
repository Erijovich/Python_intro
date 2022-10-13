# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def input_day():
    a = (input('Введите номер дня недели - '))
    try:
        return int(a)
    except:
        print('Нужно ввести целое число от 1 до 7')
        return input_day()

def check_day():
    a = input_day()
    if 0<a<6:
        return 'будень'
    elif 5<a<8:
        return 'выходной'
    else:
        print('Нужно ввести целое число от 1 до 7')
        return check_day()

print(check_day())

""" 
# тут , похоже, и проверка try не нужна..

def input_day():
    return (input('введите номер дня недели - '))

def check_day():
    a = input_day()
    if a == '1' or a == '2' or a == '3' or a == '4' or a == '5':
        return 'будень'
    elif a == '6' or a == '7':
        return 'выходной'
    else:
        print('Нужно ввести целое число от 1 до 7')
        return check_day()
"""