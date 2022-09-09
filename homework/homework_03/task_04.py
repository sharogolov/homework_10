# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import task_01 as name

def function_transfer(num: int) -> int:
    '''
    Преобразование положительного десятичного числа в двоичное
    '''
    if num == 0:
        return 0
    num_two = ''
    while num > 0:
        num_two = str(num % 2) + num_two
        num //= 2
    return int(num_two)

number = abs(name.get_number('Введите десятичное число, это должно быть целое число: '))
result = function_transfer(number)
print(result)
