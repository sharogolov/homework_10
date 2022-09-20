# Дана последовательность чисел. Получить список 
# уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from os import system
system("cls")

# import random
import function as fun

def sorting(f, list_input):
    return [x for x in list_input if f(x)]

number = abs(fun.get_number('Введите размер списка, это должно быть целое число: '))
list_number = fun.get_list(number)
print('Исходный список', list_number)
list_result = sorting(lambda x: list_number.count(x) == 1, list_number)
print('Список уникальных элементов', list_result)