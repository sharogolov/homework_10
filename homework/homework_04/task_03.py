# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

from os import system
system("cls")

import random

def get_number(input_string:str)->int:
    '''
    Получение числа
    '''
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print('Это не то ...')

def get_list(num:int)-> list:
    '''
    Создаем список
    '''
    list_num = [random.randint(-10, 10) for _ in range(num)]
    return list_num

def get_list_uique(list_num:list)->list:
    '''
    Создание списка из неповторяющихся элементов
    исходного списка
    '''
    list_uique = []
    for i in list_num:
        if i in list_uique:
            continue
        list_uique.append(i)
    return list_uique 


number = abs(get_number('Введите размер списка, это должно быть целое число: '))
list_number = get_list(number)
print('Исходный список', list_number)
# list_number = [1, 2, 3, 5, 1, 5, 3, 10]
list_result = get_list_uique(list_number)
print('Список неповторяющихся элементов', list_result)
