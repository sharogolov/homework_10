# Задана натуральная степень k. Сформировать 
# случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

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

def write_file(polynomial):
    '''
    Запись многочлена в фаил
    '''
    f = open('file_04_04.txt', 'w')
    f.write(str(polynomial))
    f.close()

number = abs(get_number('Введите степень многочлена, это должно быть целое число: '))
string = get_polynomial(number)
print('Создан многочлен:\n', string)
write_file(string)