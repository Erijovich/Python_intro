# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_bool_num(text):
    a = (input(text))
    try:
        if 0 <= int(a) < 2:
            return bool(int(a))
        else:
            print('Нужно ввести 1 или 0')
            return input_bool_num(text)
    except:
        print('Нужно ввести 1 или 0')
        return input_bool_num(text)

x = input_bool_num('Введите Х: ')
y = input_bool_num('Введите Y: ')
z = input_bool_num('Введите Z: ')

print ('Если присмотреться внимательно: в левой части, если хотя бы одно значение истинно, то вся часть ложна, '
     + 'в правой же части точно так же, если хотя бы одно значение истинно , то через отриание оно ложно '
     + 'и через логическое и, всё выражение ложно. Таким образом это выражение всегда истинно')

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print ('true')
else:
    print ('false')




# здесь попытка сделать допзащиту, что бы был экстренный выход, но надо добавлять ещё
""" 
def input_bool_num(text, counter):
    if counter > 4:
        print('За пять попыток, ничего не получилось, возможно не работает клава, поэтому делаем экстренное прерывание')
        return
    counter += 1
    a = (input(text))
    try:
        if 0 <= int(a) < 2:
            return bool(int(a))
        else:
            print('Нужно ввести 1 или 0')
            return input_bool_num(text, counter)
    except:
        print('Нужно ввести 1 или 0')
        return input_bool_num(text, counter)


x = input_bool_num('Введите Х: ', 0)
y = input_bool_num('Введите Y: ', 0)
z = input_bool_num('Введите Z: ', 0)

# print(f'{x} {y} {z}') 
"""