
import entry_csv as ec
import entry_txt as et
import read_csv as rc
import read_txt as tc
import view as v
import search as s

def button_click():
    print('''Выберите нужное действие:
    1 добавление записи в телефонную книгу
    2 поиск записи в телефонной книге
    3 просмотр телефонной книги''')
    action = int(v.get_action(':'))
    if action == 1:
        ec.write_cvs()
    elif action == 2:
        lst = rc.read_csv()
        result = s.search(lst)
        v.view_data(result)
    else:
        result = rc.read_csv()
        v.view_data(result)

