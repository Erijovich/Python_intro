# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

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
    # list = [random.randint(min, max) for _ in range(random.randrange(1, total))]
    list = [random.randint(min, max) for _ in range(total)]
    return list

def find_only_elements(list):
    only_elements = []
    for element in list:
        if element not in only_elements:
            only_elements.append(element)
    return only_elements

exeption_msg = 'Только целое цисло!'
total = input_number('Для задания последовательности случайных чисел укажите максимальное кол-во элементов: ', exeption_msg)
max = input_number('Укажите максимальное возможное значение элемента: ', exeption_msg)
min = input_number('Укажите минимально возможное значение элемента: ', exeption_msg)

list = create_random_list(min, max, total)
print(f'заданная последовательность: {list}')
print(f'Уникальные элементы последовательности: {find_only_elements(list)}')
