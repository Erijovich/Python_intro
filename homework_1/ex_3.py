# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def num_input (text):
    a = input(text)
    try:
        return(float(a))
    except:
        print("Нужно имено число!")
        return num_input(text)

x = num_input('Введите координату X: ')
y = num_input('Введите координату Y: ')

# брррр.... можно же лучше, не?
if   x>0 and y>0:    text = 'в первой четверти'
elif x<0 and y>0:    text = 'во второй четверти'
elif x<0 and y<0:    text = 'в третьей четверти'
elif x>0 and y<0:    text = 'в четвёртой четверти'
elif x==0 and y==0:  text = 'в начале координат' 
elif x==0 and y!=0:  text = 'на оси ординат'
elif x!=0 and y==0:  text = 'на оси абсцисс'

print(f'Точка с координатами ({x}, {y}) лежит {text}')
