# Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй и 
# предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from typing import List
import task_01 as name


def list_multiplication(list_num:List) -> List:
    '''
    Получение списка состоящего из произведения пар элементов
    первоначального списка.
    '''
    list_new = [list_num[i] * list_num[-(i + 1)] for i in range(len(list_num) // 2)]
    if len(list_num) % 2 != 0:
        list_new.append(list_num[(len(list_num) //2)] ** 2)
    return list_new

number = abs(name.get_number('Введите размер списка, это должно быть целое число: '))
list_number = name.get_list(number)
print(list_number)
list_result = list_multiplication(list_number)
print(list_result)