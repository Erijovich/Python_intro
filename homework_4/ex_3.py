#задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#*Пример:*
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def input_natural_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        if int(user_input) > 0:
            return(int(user_input))
        print(exeption_msg)       
    except ValueError:
        print(exeption_msg)
    return input_natural_number(invite_msg, exeption_msg)  


def input_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        return(int(user_input))
    except ValueError as error:
        print(f'{exeption_msg}\nОписание ошибки: {error}')
    return input_number(invite_msg, exeption_msg)  


def write_poly_to_file(polynomial):
    with open('polynomial.txt', 'w') as data:
        data.write(polynomial)


def create_poly_factors(power, min, max):
    if max < min: min,max = max,min
    factors_list = [random.randint(min, max) for _ in range(0, power+1)]
    if factors_list[-1] == 0:
        factors_list[-1] = random.randint(min, max)
    return factors_list


def create_polynomial(factors_list):
    polynomial = []
    for i in range(len(factors_list)):
        if factors_list[i] != 0:
            a = f'{factors_list[i]}*x^{i}'
            polynomial.append(a)
        else:
            polynomial += ''
    polynomial = polynomial[::-1]
    return '+'.join(polynomial).replace('+-', '-').replace('x^1', 'x').replace('*x^0', '').replace('1*x', 'x')+'=0'


exeption_msg_whole = 'Только целое цисло!'
exeption_msg_natural = 'Только натуральное цисло!'
power = input_natural_number('Введите максимальную степень многочлена: ', exeption_msg_natural)
max = input_number('Укажите максимальное возможное значение коэффициента: ', exeption_msg_whole)
min = input_number('Укажите минимально возможное значение коэффициента: ', exeption_msg_whole)

factors_list = create_poly_factors(power, min, max)
polynomial = create_polynomial(factors_list)
write_poly_to_file(polynomial)

print(f'Полученный многочлен: {polynomial}')