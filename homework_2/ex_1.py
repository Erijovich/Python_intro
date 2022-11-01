
# Задача 1. 
# Напишите программу, которая принимает на вход вещественное или 
# целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


from fractions import Fraction

def num_input (text):
    a = input(text)
    try:
        return(Fraction(a))
    except:
        print("Нужно имено число!")
        return num_input(text)

def convert_fract_to_whole(frac_num):
    if frac_num < 0 : frac_num = -frac_num # убираем возможный минус
    remnant = frac_num%1
    while remnant%1 > 0: # убираем дробную часть
        frac_num *= 10
        remnant = frac_num%1
    return frac_num
        
def num_length(n): 
    len = 0
    while n > 0:
        n //= 10
        len += 1
    return len

def sum_of_nums(len):
    sum = 0
    while len > 0:
        a = n%(10**(len))// (10**(len-1))
        len -= 1
        sum = sum + a
    return sum


n = convert_fract_to_whole(num_input("Введите число: "))
print (f"Сумма цифр равна: {sum_of_nums(n)}")

