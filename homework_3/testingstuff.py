# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# выберете способ задания списка - ввод вручную или путём редактирования txt-файла
# улучшить инпут нумбер так, что бы посылать в него диапазон проверки, по анаогии с "работа со строками"
# от -1 до 13, от 0.0 до 100000.(9), от минус бесконечность до 15, любой диапазон лишь бы целые
# [-1:13] , [0.0, 100000.(9)], [-:15], [-:+, true] хз..

# попробуем полноценно с файлами разобраться

def input_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        return(int(user_input))
    except ValueError as error:
        print(f'{exeption_msg}\nОписание ошибки: {error}')
    return input_number(invite_msg, exeption_msg)  

def get_list_from_input():
    array = []
    next_input = input_number('введите целое число: ', 'только целое число!')
    while next_input != '':
        array.append(next_input)
        next_input = input_number('введите целое число: ', 'только целое число!')
    
    return array

def get_list_from_file(path):
    with open(path, 'r') as f:
        return f.read().split('\n')
# для сумматора совершенно не важно что стоит на чётных позициях, лишь бы нечётные были числами, и надо флоат делать

def odd_sum(list): # поиск ошибки тут 
    sum = 0
    for i in list:
        try:
            sum += int(i)
        except:
            sum = 'ошибка'
    return sum

def intput_type_choise():
    invite_msg = 'Выберете способ задания списка - ввод вручную [1] или через txt-файл [2] (для выхода, нажми [3]): '
    exeption_msg = 'Некорректный ввод. На ввод принимаем только числа 1, 2 или 3'
    flag = True
    while flag:
        user_choise = input_number(invite_msg, exeption_msg)
        if 1<= user_choise <=3:
            return user_choise
        else:
            print(exeption_msg)

def input_list_type (num):
    if num == 1:
        sum = odd_sum(get_list_from_input())
    elif num == 2:
        sum = odd_sum(get_list_from_file(path))
    return sum
    

intput_type_choise()
# print(f'Сумма элементов на нечётнык позициях равна = {find_odd_sum_in_list()}')



""" 
path = 'str.txt'
list2 = get_list_from_file(path)


path = 'file1.txt'
data = open(path, 'r')
prod = 1
for line in data:
    prod *= list1[int(line)]
print(prod)
data.close()

 """



# пропверим рандом
def create_random_list(min, max, total):
    list = [random.randint(min, max) for _ in range(random.randrange(1, total))]
    return list

exeption_msg = 'Только целое цисло!'
total = input_number('Для задания случайного массива чисел укажите максимальное возможное кол-во элементов: ', exeption_msg)
max = input_number('Укажите максимальное возможное значение элемента: ', exeption_msg)
min = input_number('Укажите минимально возможное значение элемента: ', exeption_msg)

list = create_random_list(min, max, total)
