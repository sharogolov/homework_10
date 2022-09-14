# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from os import system
system("cls")

import random
import function as name

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


number = abs(name.get_number('Введите размер списка, это должно быть целое число: '))
list_number = name.get_list(number)
print('Исходный список', list_number)
list_result = get_list_uique(list_number)
print('Список неповторяющихся элементов', list_result)