
import logging
import csv
import os
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


# Определяем константы этапов разговора
CHOICE, WRITE_CVS, SEARCH, FIO, TEL, SEARCH_DELETE = range(6)
    

# функция обратного вызова точки входа в разговор


def start(update, _):
    update.message.reply_text(
        'Добро пожаловать в телефонную книгу.\n Выберите нужное действие:')
    update.message.reply_text(
        '1 - добавление записи в телефонную книгу \n'
        '2 - поиск записи в телефонной книге \n'
        '3 - просмотр телефонной книги \n'
        '4 - удаление записи \n'
        '5 - выход')
    return CHOICE


def choice(update, context):
    user_choice = update.message.text
    if user_choice == '1':
        update.message.reply_text(
            'Фамилия Имя:')
        return FIO
    if user_choice == '2':
        context.bot.send_message(
            update.effective_chat.id, 'Введите значение для поиска: ')
        return SEARCH
    if user_choice == '3':
        text = read_csv()
        context.bot.send_message(
            update.effective_chat.id, text)
        return start(update, context)
    if user_choice == '4':
        context.bot.send_message(
            update.effective_chat.id, 'Введите значение для удаления: ')
        return SEARCH_DELETE    
    if user_choice == '5':
        return cancel(update, context)
    
def fio(update, context):
    lst = []
    text = update.message.text
    lst.append(text)
    update.message.reply_text(
            'Номер телефона: ')
    with open ('phone_book_bot.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator=',')
        file_writer.writerow(lst)
    return TEL

def tel(update, context):
    lst = []
    text = update.message.text
    lst.append(text)
    update.message.reply_text(
            'Комментарий: ')
    with open ('phone_book_bot.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator=',')
        file_writer.writerow(lst)
    return WRITE_CVS

def write_cvs(update, context):
    '''
    Запись в csv фаил
    '''
    lst = []
    text = update.message.text
    lst.append(text)
    with open ('phone_book_bot.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
        file_writer.writerow(lst)
    return start(update, context)

def search(update, context):
    '''
    Поиск в телефонной книге
    '''
    text = update.message.text
    lst_input = read_csv_search()
    line_output = ''
    for line in lst_input:
        if text in line:
            line_output += line + '\n'
    update.message.reply_text(line_output)
    return start(update, context)

def search_delete(update, context):
    text = update.message.text
    with open('phone_book_bot.csv', encoding='utf-8') as r_file:
            with open ('test_bot.csv', mode = 'w', encoding='utf-8') as w_file:
                line_reader = csv.reader(r_file, delimiter=',')
                line_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
                for line in line_reader:
                    str = ' '.join(line)
                    if text in str:
                        update.message.reply_text(str)
                        update.message.reply_text('Запись будет удалена')
                        continue
                    line_writer.writerow(line)
    os.remove('phone_book_bot.csv')
    os.rename('test_bot.csv', 'phone_book_bot.csv')
    return start(update, context)

def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('phone_book_bot.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        contact =''
        for line in reader:
            contact += ' '.join(line)+'\n'
            #contact_list.append(line)
    return contact

def read_csv_search():
    with open('phone_book_bot.csv', encoding='utf-8') as r_file:
        file_reader_1 = csv.reader(r_file, delimiter=',')
        file_reader = []
        for line in file_reader_1:
            line = ' '.join(line)
            file_reader.append(line)
        return file_reader

def cancel(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - заходи.',
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями CHOICE, WRITE_CVS, SEARCH, FIO, TEL, SEARCH_DELETE
    conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            WRITE_CVS: [MessageHandler(Filters.text, write_cvs)],
            SEARCH: [MessageHandler(Filters.text, search)],
            FIO: [MessageHandler(Filters.text, fio)],
            TEL: [MessageHandler(Filters.text, tel)],
            SEARCH_DELETE: [MessageHandler(Filters.text, search_delete)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()