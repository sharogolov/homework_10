# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной 
# позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
# ответ: 12

from typing import List
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

def get_list(num:int)-> List:
    '''
    Создаем список
    '''
    list_num = [random.randint(-10, 10) for _ in range(num)]
    return list_num

def sun_number(list_number:List) -> int:
    '''
    Получение суммы элементов списка стоящих
    на нечетных позициях
    '''
    list_new = [list_number[i] for i in range(len(list_number)) if i % 2 != 0]
    return sum(list_new)

if __name__=='__main__':    
    number = abs(get_number('Введите размер списка, это должно быть целое число: '))
    list_number = get_list(number)
    print(list_number) 
    result = sun_number(list_number)
    print(result)
