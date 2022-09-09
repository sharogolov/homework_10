# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 или 19
# - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


from typing import List
import task_01 as name
import random

def get_list(num:int)-> List:
    '''
    Создаем список вещественных чисел
    '''
    list_num = [round(random.random()*10, 2) for _ in range(num)]
    return list_num

def difference_num(list_number:List) -> int:
    '''
    Получение разницы между максимальным и минимальным 
    значением дробной части элементов списка. 
    '''
    list_new = [i % 1 for i in list_number]
    difference = int((max(list_new) - min(list_new))*100)
    return difference


number = abs(name.get_number('Введите размер списка, это должно быть целое число: '))
#list_num = [4.07, 5.1, 8.2444, 6.98]
list_num = get_list(number)
print(list_num)
result = difference_num(list_num)
print(result)