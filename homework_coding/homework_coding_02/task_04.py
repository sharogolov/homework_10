# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime
# (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import datetime

def get_number(input_string):
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number()

def random_num(min_elenent, max_element):
    num = int(datetime.datetime.now().strftime('%f')) / 1000000
    num = int(num * (max_element - min_elenent) + min_elenent)
    return num

min_number = get_number('Введите нижнюю границу: ')
max_number = get_number('Введите верхнюю границу: ')
result =random_num(min_number, max_number) 
print(f'Случайное число от {min_number} до {max_number} = {result}')

