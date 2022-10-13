# задача 4 HARD необязательная Напишите простой калькулятор, который считывает 
# с пользовательского ввода три строки: первое число, второе число и операцию, 
# после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") 
# и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

def num_input (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        return(float(user_input))
    except:
        print(exeption_msg)
        return num_input(invite_msg, exeption_msg)

def operation_input(invite_msg, exeption_msg):
    user_input = input(invite_msg)
    if user_input in exeption_msg:
        return user_input
    else:
        print(exeption_msg)
        return operation_input(invite_msg, exeption_msg)

def primitive_calculatior():
    operation_list = ['+', '-', '/', '*', 'mod', 'pow', 'div'] 
    exeption_msg = 'Нужно имено число!'
    x = num_input('Введите первое число: ', exeption_msg)
    operation = operation_input('Введите арифметическую операцию: ', f'Поддерживаемые операции: {operation_list}')
    y = num_input('Введите второе число: ', exeption_msg)

    # кошмарно загруженно выглядит...
    
    result = 0 
    if (operation == operation_list[2] or operation == operation_list[4] or operation == operation_list[6]) and y == 0: result = '' # ААААА
    elif operation == operation_list[0]: result = x + y
    elif operation == operation_list[1]: result = x - y
    elif operation == operation_list[2]: result = x / y
    elif operation == operation_list[3]: result = x * y
    elif operation == operation_list[4]: result = x % y
    elif operation == operation_list[5]: result = x ** y
    elif operation == operation_list[6]: result = x // y

    if result == '': print('Делить на ноль опасно для целостности пространства-временни')
    else: print(f'{x} {operation} {y} = {result}')

    if input('Повторим? (1 - да, любой другой ввод - выход): ') == '1' : primitive_calculatior()

primitive_calculatior()

