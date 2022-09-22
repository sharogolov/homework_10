import view as v

def write_txt():
    '''
    Запись в txt фаил
    '''
    lst = []
    text = v.get_action('Фамилия Имя: ')
    lst.append(text)
    text = v.get_action('Номер телефона: ')
    lst.append(text)
    text = v.get_action('Комментари: ')
    lst.append(text)
    with open('phone_book.txt', "a", encoding='utf-8') as file:
        for  line in lst:
            file.write(line + ' ')
        file.write('\n')

 
