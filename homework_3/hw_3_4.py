#Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
#*Пример:*
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def input_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        return(int(user_input))
    except ValueError as error:
        print(f'{exeption_msg}\nОписание ошибки: {error}')
    return input_number(invite_msg, exeption_msg)  

def decimal_binary_converter(num):
    binary_list = []
    while num != 0:
        num_bin = num % 2
        num = num // 2
        binary_list.append(num_bin)
    binary_list = binary_list[::-1]
    return ''.join(str(elem) for elem in binary_list)

exeption_msg = 'Только целое цисло!'
n = input_number('введите целое десятичное число для преобразования в двоичное: ', exeption_msg)
print(f'в двоичной форме получается так: {decimal_binary_converter(n)}')