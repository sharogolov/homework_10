# 2 - Напишите программу, которая принимает на вход число N и выдает
# набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def list_element():
    try:
        num = int(input('Введите число: '))
        list_number = []
        element = 1
        for i in range(1, num + 1):
            element *= i
            list_number.append(element)
        return list_number
    except(ValueError):
        return list_element()

list_result = list_element()
print(list_result)
