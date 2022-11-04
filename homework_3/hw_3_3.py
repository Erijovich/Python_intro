# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def input_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        return(int(user_input))
    except ValueError as error:
        print(f'{exeption_msg}\nОписание ошибки: {error}')
    return input_number(invite_msg, exeption_msg)  

def create_random_list(min, max, total):
    if max<min: min,max = max,min
    list = [round(random.uniform(min, max), 3) for _ in range(random.randrange(3, total))]
    return list

     

def fractions_list(list):
    fract_list = [round(list[i]%1, 2) for i in range(len(list))]
    return fract_list

def max_sub_min(fract_list):
    min_fract = fract_list[0]
    max_fract = fract_list[0]
    for i in range(1, len(fract_list)):
        if fract_list[i] < min_fract: min_fract = fract_list[i]
        if fract_list[i] > max_fract: max_fract = fract_list[i]
    sub = max_fract - min_fract
    return round(sub, 2)

exeption_msg = 'Только целое цисло!'
total = input_number('Для задания случайного массива чисел укажите максимальное возможное кол-во элементов: ', exeption_msg)
max = input_number('Укажите максимальное возможное значение элемента: ', exeption_msg)
min = input_number('Укажите минимально возможное значение элемента: ', exeption_msg)

list = create_random_list(min, max, total)
print(f'заданный список: {list}')
frac_list = fractions_list(list)
print(f'дробные части заданного списка: {frac_list}')
print(f'максимальная разница: {max_sub_min(frac_list)}')
