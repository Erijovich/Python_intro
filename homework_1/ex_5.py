# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается 
# с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import random

def input_natural_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        if int(user_input) > 0:
            return(int(user_input))
        print(exeption_msg)       
    except:
        print(exeption_msg)

    return input_natural_number(invite_msg, exeption_msg)  

    
def input_whole_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        return(int(user_input))
    except:
        print(exeption_msg)
        return input_whole_number(invite_msg, exeption_msg) 

def table_create(rows, cols, min, max):
    if max > min: max, min = min, max
    table = []
    for i in range(rows):
        table_rows = []
        for j in range(cols):
            table_rows.append(int(min + (max-min)*random()))
        table.append(table_rows)
    return table

def table_sorting(table):
    # расплетаем табличку в одномерный массив
    monoarray = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            monoarray.append(table[i][j])
   
    array_sorting(monoarray) 

    # Обратно сплетаем одномерный массив в табличку
    counter = 0
    sorted_table = []
    for i in range(len(table)):
        sorted_table_row = []
        for j in range(len(table[i])):
            sorted_table_row.append(monoarray[counter])
            counter +=1
        sorted_table.append(sorted_table_row)

    return sorted_table

def array_sorting(array):
    iteration = 0
    for i in range(len(array)):
        min_el = array[iteration]
        min_pos = iteration
        for j in range(iteration, len(array)):
            if array[j] < min_el:
                min_el = array[j]
                min_pos = j                  
        array[iteration], array[min_pos] = array[min_pos], array[iteration]
        iteration += 1


# основной код
exeption_msg_1 = 'Только натуральные числа!'
exeption_msg_2 = 'Только целые числа!'

print('Создание, наполнение псевдослучайными числами и сортировка прямоугольного массива')
print('Укажите размер массива')
x = input_natural_number('Количество строчек: ', exeption_msg_1)
y = input_natural_number('Количество столбцов: ', exeption_msg_1)
min = input_whole_number('Укажите минимальное значение: ', exeption_msg_2)
max = input_whole_number('Укажите максимальное значение: ', exeption_msg_2)

matrix = table_create(x,y,min,max) # задаём матрицу

for i in range (len(matrix)):
    print(matrix[i])

matrix = table_sorting(matrix) # сортируем матрицу

print('___________________')
for i in range (len(matrix)):
    print(matrix[i])
