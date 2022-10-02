import csv
import view as v
import os

def write_cvs():
    '''
    Запись в базу данных
    '''
    lst = []
    text = v.get_action('Фамилия: ')
    lst.append(text)
    text = v.get_action('Имя: ')
    lst.append(text)
    text = v.get_action('Отчество: ')
    lst.append(text)
    text = v.get_action('Возраст: ')
    lst.append(text)
    text = v.get_action('Должность: ')
    lst.append(text)
    text = v.get_action('Оклад: ')
    lst.append(text)
    with open ('baza.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
        file_writer.writerow(lst)
        


def search():
    '''
    Поиск
    '''
    num = v.get_search_choice()
    count = 0
    if str(num) in '0124':
        value = v.get_search_value(num)
        with open('baza.csv', encoding='utf-8') as r_file:
            file_reader_1 = csv.reader(r_file, delimiter=',')
            for line in file_reader_1:
                if line[num] == value:
                    v.view_data_value(line)
                    count += 1
    else:
        value_min, value_max = v.get_search_value(num)
        with open('baza.csv', encoding='utf-8') as r_file:
            file_reader_1 = csv.reader(r_file, delimiter=',')
            for line in file_reader_1:
                if value_min <= int(line[num]) <= value_max:
                    v.view_data_value(line)
                    count += 1        
    if count == 0:
        v.view_data_none()


def read_csv():
    '''
    Чтение из базы данных
    '''
    with open('baza.csv', encoding='utf-8') as r_file:
        file_reader_1 = csv.reader(r_file, delimiter=',')
        file_reader = []
        for line in file_reader_1:
            line = ' '.join(line)
            file_reader.append(line)
        v.view_data(file_reader)


def get_rewrite():
    '''
    Редактирование
    '''
    num = v.get_search_choice()
    count = 0
    if str(num) in '0124':
        value = v.get_search_value(num)
        with open('baza.csv', encoding='utf-8') as r_file:
            with open ('temp.csv', mode = 'w', encoding='utf-8') as w_file:
                line_reader = csv.reader(r_file, delimiter=',')
                line_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
                for line in line_reader:
                    if line[num] == value:
                        v.view_data_value(line)
                        count += 1
                        while True:
                            index = v.get_choice_rewrite()
                            if index == 6:
                                break
                            else:
                                line[index] = v.get_action('Введите новое значение: ')
                    line_writer.writerow(line)
        os.remove('baza.csv')
        os.rename('temp.csv', 'baza.csv') 
    else:
        value_min, value_max = v.get_search_value(num)
        with open('baza.csv', encoding='utf-8') as r_file:
            with open ('temp.csv', mode = 'w', encoding='utf-8') as w_file:
                line_reader = csv.reader(r_file, delimiter=',')
                line_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
                for line in line_reader:
                    if value_min <= int(line[num]) <= value_max:
                        v.view_data_value(line)
                        count += 1
                        while True:
                            index = v.get_choice_rewrite()
                            if index == 6:
                                break
                            else:
                                line[index] = v.get_action('Введите новое значение: ')
                    line_writer.writerow(line)
        os.remove('baza.csv')
        os.rename('temp.csv', 'baza.csv')
    if count == 0:
        v.view_data_none()

   

def get_remove():
    '''
    Удаление
    '''
    num = v.get_search_choice()
    count = 0
    if str(num) in '0124':
        value = v.get_search_value(num)
        with open('baza.csv', encoding='utf-8') as r_file:
            with open ('temp.csv', mode = 'w', encoding='utf-8') as w_file:
                line_reader = csv.reader(r_file, delimiter=',')
                line_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
                for line in line_reader:
                    if line[num] == value:
                        v.view_data_value(line)
                        count += 1
                        print('Запись будет удалена')
                        continue
                    line_writer.writerow(line)
        os.remove('baza.csv')
        os.rename('temp.csv', 'baza.csv') 
    else:
        value_min, value_max = v.get_search_value(num)
        with open('baza.csv', encoding='utf-8') as r_file:
            with open ('temp.csv', mode = 'w', encoding='utf-8') as w_file:
                line_reader = csv.reader(r_file, delimiter=',')
                line_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
                for line in line_reader:
                    if value_min <= int(line[num]) <= value_max:
                        v.view_data_value(line)
                        count += 1
                        print('Запись будет удалена')
                        continue
                    line_writer.writerow(line)
        os.remove('baza.csv')
        os.rename('temp.csv', 'baza.csv')
    if count == 0:
        v.view_data_none()



            
