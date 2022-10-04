
from os import system
from uuid import NAMESPACE_X500
system("cls")
import random

import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
GET_PLAYER,  GET_CANDY, GAME_CANDY, LAST_MOVE, PLAY_GAMER = range(5)

# функция обратного вызова точки входа в разговор
def start(update, _):    
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Добро пожаловать в игру "Sweet Life".'
        'Правила нашей игры:'
        'На столе лежат конфеты.'
        'Играют два игрока делая ход друг после друга.'
        'Первый ход определяется жеребьёвкой.'
        'За один ход можно забрать не более чем'
        'определенное количество конфет.'
        'Выигрывает игрок сделавший последний ход'
        '- он забирает все конфеты.'
        'Меня зовут Нафаня и я буду Вашим соперником.\n'
        'Команда /cancel, чтобы прекратить игру.')
    update.message.reply_text('Введите количество конфет с'
        'которым будем играть: ')    
    # переходим к этапу `GET_CANDY`, это значит, что ответ
    # отправленного сообщения в виде строки 
    # будет определен в виде значения ключа `GET_CANDY`
    return GET_CANDY

def get_candy(update, context):
    user = update.message.from_user
    logger.info("Кол-во конфет: %s: %s", user.first_name, update.message.text)
    get_candy = update.message.text
    if get_candy.isdigit():
        get_candy = int(get_candy)
        context.user_data['get_candy'] = get_candy
        update.message.reply_text(f'На столе {get_candy} конфет.\n')
        update.message.reply_text('Введите максимальное количество конфет'
            'которое можно взять за один ход.'
            'Оно должно быть меньше количества конфет на столе.\n')
        return GAME_CANDY
    else:
        update.message.reply_text('Это не число. Введите число.')

def game_candy(update, context):
    user = update.message.from_user
    logger.info("Кол-во конфет за ход: %s: %s", user.first_name, update.message.text)
    game_candy = update.message.text
    if game_candy.isdigit():
        game_candy = int(game_candy)
        get_candy = context.user_data.get('get_candy')
        if game_candy < get_candy and game_candy > 0:
            context.user_data['game_candy'] = game_candy
            update.message.reply_text(f'За один ход можно взять от 1 до {game_candy} конфет.')
            update.message.reply_text('Игрок, как к Вам обращаться?')
            return GET_PLAYER
        else:
            update.message.reply_text(f'Количество конфет должно быть меньше {get_candy}.') 
    else:
        update.message.reply_text('Это не число. Введите число.')        

def get_player(update, context):
    '''
    Определение первого хода
    '''
    user = update.message.from_user
    logger.info("Обращение к игроку: %s: %s", user.first_name, update.message.text)
    name_0 = update.message.text
    context.user_data['name_0'] = name_0
    name_1 = 'Нафаня'
    context.user_data['name_1'] = name_1
    update.message.reply_text('Сейчас мы разыграем право первого хода...')
    temp = random.randint(0, 1)
    if temp == 0:
        gamer = name_0
        context.user_data['gamer'] = gamer
        update.message.reply_text(f'И первым у нас берет конфеты {gamer}!')
        context.bot.send_message(update.effective_chat.id, f'{name_0} сколько берете конфет?')
        return PLAY_GAMER        
    else:
        gamer = name_1
    context.user_data['gamer'] = gamer
    update.message.reply_text(f'И первым у нас берет конфеты {gamer}!')
    return play_bot(update, context)

def play_gamer(update, context):
    # name_1 = context.user_data.get('name_1')
    get_candy = context.user_data.get('get_candy')
    game_candy = context.user_data.get('game_candy')
    user = update.message.from_user
    logger.info("Пользователь взял: %s: %s", user.first_name, update.message.text)
    move = update.message.text 
    if move.isdigit():
            move = int(move)
            if move <= game_candy:
                get_candy -= move
                update.message.reply_text(f'У нас осталось {get_candy} конфет')
                context.user_data['get_candy'] = get_candy
                if get_candy <= game_candy:
                    return LAST_MOVE
                return play_bot(update, context)    
            else:
                update.message.reply_text(f'Максимальное количество конфет: {game_candy}')
    else:
        update.message.reply_text('Это не число. Введите число.')

def play_bot(update, context):
    name_0 = context.user_data.get('name_0')
    name_1 = context.user_data.get('name_1')
    get_candy = context.user_data.get('get_candy')
    game_candy = context.user_data.get('game_candy')
    if get_candy > game_candy:
        move = random.randint(1, game_candy + 1)
        update.message.reply_text(f'Я беру {move} конфет')
        get_candy -= move
        update.message.reply_text(f'У нас осталось {get_candy} конфет')
        context.user_data['get_candy'] = get_candy
        context.bot.send_message(update.effective_chat.id, f'{name_0} сколько берете конфет?')
        if get_candy <= game_candy:
            update.message.reply_text(f'{name_0} вы можете взять от 1 до {get_candy} конфет')
            return LAST_MOVE
        else:
            return PLAY_GAMER
    else:
        move = get_candy
        update.message.reply_text(f'Я беру {move} конфет')
        update.message.reply_text(f'Победитель {name_1}!!!')
        update.message.reply_text('Game over')
        return ConversationHandler.END

def last_move(update, context):
    '''
    Получение количества конфет
    для последнего хода
    '''
    gamer = context.user_data.get('gamer')
    name_0 = context.user_data.get('name_0')
    name_1 = context.user_data.get('name_1')
    get_candy = context.user_data.get('get_candy')
    user = update.message.from_user
    logger.info("Пользователь взял: %s: %s", user.first_name, update.message.text)
    move = update.message.text
    if move.isdigit():
        move = int(move)
        if move == get_candy:
            update.message.reply_text(f'Победитель {name_0}!!!')
            update.message.reply_text('Game over')
            return ConversationHandler.END
        elif move < get_candy:    
            get_candy -= move
            update.message.reply_text(f'У нас осталось {get_candy} конфет')
            context.user_data['get_candy'] = get_candy
            gamer = name_1
            context.user_data['gamer'] = gamer
            winner = name_0
            context.user_data['winner'] = winner
            return LAST_MOVE
        else:
            update.message.reply_text(f'Максимальное количество конфет: {get_candy}')
    else:
        update.message.reply_text('Это не число. Введите число.')


# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END



if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    bot = Bot(token=TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GET_PLAYER,  GET_CANDY, GAME_CANDY, LAST_MOVE, PLAY_GAMER
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            GET_PLAYER: [MessageHandler(Filters.text, get_player)], 
            GET_CANDY: [MessageHandler(Filters.text, get_candy)],
            GAME_CANDY: [MessageHandler(Filters.text, game_candy)],
            LAST_MOVE: [MessageHandler(Filters.text, last_move)],
            PLAY_GAMER: [MessageHandler(Filters.text, play_gamer)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()