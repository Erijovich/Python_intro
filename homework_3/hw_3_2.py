#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

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
    list = [random.randint(min, max) for _ in range(random.randrange(1, total))]
    return list

def center_finder(list):
    if len(list) % 2 == 0:
        center = int(len(list)/2)
    else:
        center = int((len(list)+1)/2)
    return center

def list_sum(list, n):
    list_sum = []
    for i in range(n):
        sum = list[i] * list[-(i+1)]
        list_sum.append(sum)
    return list_sum

exeption_msg = 'Только целое цисло!'
total = input_number('Для задания случайного массива чисел укажите максимальное возможное кол-во элементов: ', exeption_msg)
max = input_number('Укажите максимальное возможное значение элемента: ', exeption_msg)
min = input_number('Укажите минимально возможное значение элемента: ', exeption_msg)


list = create_random_list(min, max, total)
print(f'заданный список: {list}')
center = center_finder(list)
print(center)
print(f'произведение пар чисел списка: {list_sum(list, center)}')