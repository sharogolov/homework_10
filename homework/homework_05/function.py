
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

def write_file(line:str, name:str):
    '''
    Запись строк в фаил
    '''
    with open(name, 'w', encoding="utf-8") as f:
        f.write(line) 

def read_file(name:str)->str:
    '''
    Чтение из файла
    '''
    with open(name, 'r', encoding="utf-8") as f:
        data = f.read()
        return data


