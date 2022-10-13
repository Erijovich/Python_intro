# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается 
# с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10


def input_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        if int(user_input) > 0:
            return(int(user_input))
        print(exeption_msg)
        return input_number(invite_msg, exeption_msg)
    except:
        print(exeption_msg)
        return input_number(invite_msg, exeption_msg)  # Не нравится, что дважды повторяется.. можно ли как-то объеденить??

def sorting():
    return


def table_min_max_sort (table):
    rows = len(table[0]) 
    cols = len(table[1]) // нет!

    x_pos = 0
    y_pos = 0

    for i in table:
        for j in i:
            if j < table [x_pox][y_pos]:
                
            print()
        print()
    
    return

    for (int m = 0; m < table.GetLength(0) * table.GetLength(1); m++) // все операции повторяем столько раз, сколько элементов в массиве 
                                                                      // наверное, можно сократить в два раза, если одновременно отсеивать
                                                                      // и минимальный и максимальный элемент в разные углы матрицы
    {
        int minPosI = 0, // позиции элемента, которые будем запоминать
            minPosJ = 0;

        for (int i = 0; i < rows; i++)  // теперь пробегаемся по массиву в поисках позиции элемента с минимальным значением
        {
            for (int j = 0; j < cols; j++) 
            {
                 if (table[i,j] < table[minPosI,minPosJ])
                {
                    minPosI = i;
                    minPosJ = j;
                } 
            }
        }
       
        int temp = table[rows-1,cols-1];  // свапаем последний элемент таблицы с минимальным, не забывая, что отсчёт массива начинается с нуля
        table[rows-1,cols-1] = table [minPosI,minPosJ];
        table[minPosI,minPosJ] = temp;

        cols-=1; // убираем крайний правый элемент в строчке. В случае, если это был последний, тогда убираем нижнюю строчку
        if (cols == 0)
        {
            cols = table.GetLength(1);
            rows -= 1;
        }
    }

exeption_msg = 'Только натуральные числа!'

print('Укажите размер массива')
x = input_number('Количество строчек: ', exeption_msg)
y = input_number('Количество столбцов: ', exeption_msg)