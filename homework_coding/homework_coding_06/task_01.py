# Определить, присутствует ли в заданном списке строк, 
# некоторое число

from os import system
system("cls")

import function as fun

# lines = ['abc', '45', 'bfgt', '10']
lines = [input('Введите элемент массива:') for _ in range (fun.get_number('Введите размер списка: '))]
num = fun.get_number('Введите число: ')
result = list(filter(lambda x: x == str(num), lines))
if result == []:
    print(f'Число {num} в списке отсутствует.')
else:
    print(f'Число {num} есть в списке.')
