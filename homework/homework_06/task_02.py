# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

import function as name
from os import system
system("cls")

def sorting_num(f, num):
    return [x for x in range(2, num + 1) if f(x)]

def sorting_list(f, list_input):
    return [x for x in list_input if f(x)]

number = abs(name.get_number('Введите целое число: '))
list_multiplier = list(sorting_num(lambda x : number % x == 0, number))
print('Список всех множителей числа', number, ':', list_multiplier)
list_result = sorting_list(lambda x: len(sorting_num(lambda y : x % y == 0, x)) == 1, list_multiplier)
print('Список простых множителей числа', number, ':', list_result)

