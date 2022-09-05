# Реализуйте алгоритм перемешивания списка.

import random
try:
    def list_number(num):
        list_number = []
        for i in range(num):
            list_number.append(random.randint(-100, 100))
        return list_number

    def method_random_list(num, list_num):
        list_random = []
        for j in range(num):
            list_random.append(random.choice(list_num))
            list_num.remove(list_random[j])
        return list_random    
    
    number = int(input('Введите количество элементов в списке: '))
    list_1 = list_number(number)
    print('Список: ', list_1)
    list_result = method_random_list(number, list_1)
    print('Перемешанный список: ', list_result)

except(ValueError):
    print('Что-то пошло не так...')
