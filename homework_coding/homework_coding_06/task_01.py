# Определить, присутствует ли в заданном списке строк, 
# некоторое число

import function as fun

string = ['abc', '45', 'bfgt', '10']
num = fun.get_number('Введите число: ')
result = list(filter(lambda x: x == str(num), string))
print(result)