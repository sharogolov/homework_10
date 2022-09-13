# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

from os import system
system("cls")

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

def multiplier_num(num: int)->list:
    '''
    Создаем список из всех множителей числа
    '''
    list_num = [i for i in range(2, num + 1) if num % i == 0]
    return list_num

def simple_number(list_num:list)->list:
    '''
    Создаем список из простых множителей числа
    '''
    list_simple = []
    for i in list_num:
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag == True:
            list_simple.append(i) 
    return list_simple           

number = abs(get_number('Введите целое число: '))
list_multiplier = multiplier_num(number)
print('Список всех множителей числа', number, ':', list_multiplier)
list_result = simple_number(list_multiplier)
print('Список простых множителей числа', number, ':', list_result)