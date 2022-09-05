# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt
#  в одной строке одно число.

import random
try:
    num = int(input('Введите количество элементов в списке: '))
    list_number = []
    
    for i in range(num):
        list_number.append(random.randint(-num, num))
    print('Список: ', list_number)

    index_1 = random.randint(0, num -1)
    index_2 = random.randint(0, num -1)

    result = list_number[index_1] * list_number[index_2]

    print(f'{list_number[index_1]} * {list_number[index_2]} = {result}')
except(ValueError):
    print('Что-то пошло не так...')