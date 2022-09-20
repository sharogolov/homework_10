
import random

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

def get_list(num:int)-> list:
    '''
    Создаем список
    '''
    list_num = [random.randint(-10, 10) for _ in range(num)]
    return list_num           