
def get_rational(string_input: str)-> str:
    '''
    Ввод рационального
    '''
    num = get_number(string_input)
    return num

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

num = get_rational('Введите число')
print(num)