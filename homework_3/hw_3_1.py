# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def input_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        return(int(user_input))
    except ValueError as error:
        print(f'{exeption_msg}\nОписание ошибки: {error}')
    return input_number(invite_msg, exeption_msg)  

def odd_sum(list): # поиск ошибки тут 
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0: sum += list[i]
    return sum


def create_random_list(min, max, total):
    if max<min: min,max = max,min
    list = [random.randint(min, max) for _ in range(random.randrange(1, total))]
    return list


exeption_msg = 'Только целое цисло!'
total = input_number('Для задания случайного массива чисел укажите максимальное возможное кол-во элементов: ', exeption_msg)
max = input_number('Укажите максимальное возможное значение элемента: ', exeption_msg)
min = input_number('Укажите минимально возможное значение элемента: ', exeption_msg)

list = create_random_list(min, max, total)
print(f'заданный список: {list}')
print(f'сумма элементов списка, стоящих на нечётной позиции: {odd_sum(list)}')

