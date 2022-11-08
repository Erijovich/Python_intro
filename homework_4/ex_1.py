# задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def input_natural_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        if int(user_input) > 0:
            return(int(user_input))
        print(exeption_msg)       
    except ValueError:
        print(exeption_msg)
    return input_natural_number(invite_msg, exeption_msg)  

def find_multipliers(n):
    multipliers = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            multipliers.append(i)
        i += 1
    if n > 1:
        multipliers.append(n)
    return multipliers


exeption_msg = 'Только натуральное цисло!'
n = input_natural_number('Введите натуральное число: ', exeption_msg)
print(find_multipliers(n))