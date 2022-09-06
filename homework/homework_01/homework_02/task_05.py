# Реализуйте алгоритм перемешивания списка.

import random
def get_number(input_string):
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number()

def list_random(num):
    list_element = []        
    for i in range(num):
        list_element.append(random.randint(-num, num))
    return list_element

def method_random_list(num, list_num):
    list_random = []
    for j in range(num):
        list_random.append(random.choice(list_num))
        list_num.remove(list_random[j])
    return list_random    

number = get_number('Введите количество элементов в списке: ')
list_number = list_random(number) 
print('Список: ', list_number)
list_result = method_random_list(number, list_number)
print('Перемешанный список: ', list_result)

