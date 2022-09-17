
# Создайте программу для игры с конфетами человек против 
# человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет 
# нужно взять первому игроку, чтобы забрать все конфеты у 
# своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from os import system
system("cls")
import random

def get_number_game(input_string:str)->int:
    '''
    Получение количества конфет
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 < num < 29:
                return num
            else:
                print('Неправильно. Давай еще раз.')
        except ValueError:
            print('Это не то ...')

def last_move(input_string:str, number:int)->int:
    '''
    Получение количества конфет
    для последнего хода
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 < num <= number:
                return num
            else:
                print('Неправильно. Давай еще раз.')
        except ValueError:
            print('Это не то ...')

def get_player(player_0:str, player_1:str)->str:
    '''
    Определение первого хода
    '''
    print('Сейчас мы разыграем право первого хода...')
    temp = random.randint(0, 1)
    if temp == 0:
        gamer = player_0
    else:
        gamer = player_1
    print(f'И первым у нас берет конфеты {gamer}!')
    return gamer

def playng(candy:int, player:str, player_1:str, player_2:str, messages:list)->str:
    winner = ''
    while candy > 0:
        if candy == 2021 and player == player_2:
            move = 5
            print(f'Я беру {move} конфет')
            candy -= move
            player = player_1
            winner = player_2
        if candy > 28:
            if player == player_1:
                print(f'У нас {candy} конфет.')
                index = random.randint(0, 4)
                move = get_number_game(f'{player} {messages[index]}. Вы можете взять от 1 до 28: ')
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет.')
                move = 29 - move
                print(f'Я беру {move} конфет')
                candy -= move
                player = player_1
                winner = player_2
        else:
            if player == player_1:
                print(f'У нас {candy} конфет.')
                index = random.randint(0, 4)
                move = last_move(f'{player} {messages[index]}. Вы можете взять от 1 до {candy}: ', candy)
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет.')
                move = candy
                print(f'Я беру {move} конфет')
                candy -= move
                player = player_1
                winner = player_2
    return winner


print('''
Добро пожаловать в игру "Sweet Life".
Правила нашей игры:
На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Выигрывает игрок сделавший последний ход 
- он забирает все конфеты.
Меня зовут Нафаня и я буду Вашим соперником.\n''')

text_massages = ['ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'ваш ход']
name_0 = input('''Давайте знакомиться. Игрок, как к Вам обращаться?\n''')
name_1 = 'Нафаня'
gamer = get_player(name_0, name_1)
sweet = 2021
winner = playng(sweet, gamer, name_0, name_1, text_massages)
print(f'''
У нас есть победитель.
Это {winner}!!!
Наша игра закончена.''') 

