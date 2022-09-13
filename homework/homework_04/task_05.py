# Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, содержащий сумму 
# многочленов.

import random
import sympy

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

def get_polynomial(num:int)->str:
    '''
    Создание многочлена 
    '''
    x = sympy.Symbol('x')
    expr = 0
    for i in range(num + 1):
        a = random.randint(0, 100)
        if a != 0:
            expr += a * x ** i       
    return expr

def write_file(polynomial, num:int):
    '''
    Запись многочлена в фаил
    '''
    number_fail = 'file_04_05_' + str(num) + '.txt' 
    f = open(number_fail, 'w')
    f.write(str(polynomial))
    f.close()

def read_file(num:int):
    '''
    Чтение из файла
    '''
    number_fail = 'file_04_05_' + str(num) + '.txt'
    x = open(number_fail, 'r')
    polinom = sympy.sympify(x.readline())
    x.close()
    return polinom

def sum_polinom(pol_1, pol_2):
    '''
    Сложение многочленов 
    '''
    result = pol_1 + pol_2
    return result 


number = abs(get_number('Введите степень многочлена, это должно быть целое число: '))
string_1 = get_polynomial(number)
print('Создан многочлен:\n', string_1)
string_2 = get_polynomial(number)
print('Создан многочлен:\n', string_2)
write_file(string_1, 1)
write_file(string_2, 2)
polinom_1 = read_file(1)
polinom_2 = read_file(2)
polinom_result = sum_polinom(polinom_1, polinom_2)
print('Сумма 2 многочленов:\n', polinom_result)
write_file(polinom_result, 3)