# Задайте число. Составьте список чисел Фибоначчи, в том 
# числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


from typing import List
import math

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


def fibonacci_positive(num: int)->List:
    '''
    Получение списка из чисел Фибоначчи с положительными 
    индексами
    '''
    list_fibonacci = []
    a, b = 0, 1
    for i in range(num):
        a, b = b , a + b
        list_fibonacci.append(a)
    list_fibonacci.insert(0, 0)
    return list_fibonacci

def fibonacci_negativ (list_num: List)->List:
    '''
    Получение списка из чисел Фибоначчи с отрицательными 
    индексами
    '''
    list_negativ = []
    for i in range(len(list_num) - 1):
        list_negativ.append(list_num[-(1+i)] * (-1) ** (i + 1)) 
    return list_negativ       

def fibonacci_result(list_1:List, list_2:List)->List:
    '''
    Функция сложения списков
    '''
    list_end = list_2 + list_1
    return list_end

number = abs(get_number('Введите целое число для получения списка Фибоначчи: '))
list_positive = fibonacci_positive(number)
list_negativ = fibonacci_negativ(list_positive)
list_result = fibonacci_result(list_positive, list_negativ)
print('Список Фибоначчи: \n', list_result)