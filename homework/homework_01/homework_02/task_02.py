# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
try:
    def multiplication_numbers(numbers):
        list_numbers = []
        for i in range(1, int(numbers) + 1):
            list_numbers.append(math.factorial(i))
        return list_numbers   

    num = input('Введите число: ')
    result = multiplication_numbers(num)
    print(result)

except(ValueError):
    print('Что-то пошло не так...')

