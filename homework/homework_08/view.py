
def view_data(lst_input:list)->str:
    '''
    Вывод информации пользователю
    '''
    print('Список сотрудников:')
    for line in lst_input:
        print(line)

def get_action(input_string: str)-> str:
    '''
    Ввод информации от пользователя
    '''
    return input(input_string)

def get_work()-> int:
    '''
    Меню выбора действий с базой
    '''
    print('''Выберите нужное действие:
    1 добавление записи в базу
    2 поиск данных в базе
    3 редактирование записи
    4 удаление записи
    5 просмотр базы данных
    6 окончание работы ''')
    num = int(get_action(':'))
    return num 

def get_search_choice()-> int:
    '''
    Mеню параметра поиска
    '''
    print('''Выберите параметр для поиска:
    0 Фамилия
    1 Имя
    2 Отчество
    3 Возраст
    4 Должность
    5 Оклад ''')
    num = int(get_action(':'))
    return num

def get_search_value(num:int)-> str:
    '''
    Значение поиска
    '''
    if num == 0:
        value = input('Введите фамилию: ')
        return value
    elif num == 1:
        value = input('Введите имя: ')
        return value
    elif num == 2:
        value = input('Введите отчество: ')
        return value
    elif num == 3:
        value_1 = int(input('Введите минимальный значение возраста: '))
        value_2 = int(input('Введите максимальное значение возраста: '))
        return value_1, value_2
    elif num == 4:
        value = input('Введите должность: ')
        return value
    else:
        value_1 = int(input('Введите минимальный оклад: '))
        value_2 = int(input('Введите максимальный оклад: '))
        return value_1, value_2

def view_data_value(lst_input:list)->str:
    '''
    Вывод информации пользователю по поиску 
    '''
    print(*lst_input)

def view_data_none()->str:
    '''
    Вывод информации пользователю по поиску
    при нулевых результатах 
    '''
    print('Таких значений в базе не найдено')

def get_choice_rewrite()->int:
    '''
    Меню перезаписи
    '''
    print('''Выберите параметр для редактирования:
    0 Фамилия
    1 Имя
    2 Отчество
    3 Возраст
    4 Должность
    5 Оклад 
    6 Выход''')
    num = int(get_action(':'))
    return num

    