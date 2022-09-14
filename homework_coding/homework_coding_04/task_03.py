# В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

import os
os.system("cls")

def write_file(lines:list, name:str):
    '''
    Запись строк в фаил
    '''
    with open(name, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line + '\n')
    
def read_file(name:str):
    '''
    Чтение из файла
    '''
    with open(name, 'r', encoding="utf-8") as f:
        for line in f:
            print(line.strip())
          

def replace_char(name:str):
    '''
    Перезапись информации в текстовом файле
    '''
    with open(name, 'r', encoding="utf-8") as f_1, \
          open('temp.txt', 'w', encoding="utf-8") as f_2:
        for line in f_1:
            str_line = line.split()
            if float(str_line[-1]) > 4:
                f_2.write(line.upper())
            else:
                f_2.write(line)
    p = os.path.abspath(name)
    os.remove(p)
    p_1 = os.path.abspath('temp.txt')
    os.rename(p_1, p)


lines_str = ['Волков Андрей 5', 'Наталья Тарасова 5', \
              'Фредди Меркури 3', 'Денис Байцуров 4']
name_fail = 'file_task_04_03.txt' 
write_file(lines_str, name_fail) 
replace_char(name_fail)
read_file(name_fail)
