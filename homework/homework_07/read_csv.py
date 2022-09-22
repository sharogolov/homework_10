import csv

# def read_csv():
#     '''
#     Чтение из файла csv
#     '''
#     with open('phone_book.csv', encoding='utf-8') as r_file:
#         file_reader = csv.reader(r_file, delimiter=' ')
#         # for line in file_reader:
#         print(list(file_reader)) 

def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('phone_book.csv', encoding='utf-8') as r_file:
        file_reader_1 = csv.reader(r_file, delimiter=' ')
        file_reader = []
        for line in file_reader_1:
            line = ' '.join(line)
            file_reader.append(line)
        return file_reader

