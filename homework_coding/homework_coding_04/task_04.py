# Шифр Цезаря - это способ шифрования, где каждая буква 
# смещается на определенное количество символов влево или 
# вправо. При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - 
# сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - 
# сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в 
# файл шифрованный текст, а также функцию, которая спрашивает 
# ключ, считывает текст и дешифровывает его.

# print(ord('А'))
# print(ord('я'))



from os import system
system("cls")
import function as name


eng_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ru_alph = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'

def sifr_ceasar(string:str, k:int):
    '''
    Шифрование и дешифрование текста
    '''
    string_sifr = ''
    for s in string:
        if s.isalpha() and s in ru_alph:
            index = ru_alph.find(s) + k
            if index > 63:
                index += - 64
                string_sifr += ru_alph[index] 
            else:
                string_sifr += ru_alph[index]
        elif s.isalpha() and s in eng_alph:
            index = eng_alph.find(s) + k
            if index > 51:
                index += - 52
                string_sifr += eng_alph[index] 
            else:
                string_sifr += eng_alph[index]
        else:
            string_sifr += s
    return string_sifr

def write_file(string:str, name:str, num:int):
    '''
    Запись шифрованного текста в фаил
    '''
    with open(name, 'w', encoding="utf-8") as f:
        f.write(sifr_ceasar(string, num))

def read_file(name:str, num:int):
    '''
    Чтение из файла и дешифровка
    '''
    with open(name, 'r', encoding="utf-8") as f:
        string_fail = f.read()
        print('Зашифрованная фраза:\n', string_fail) 
        print()
        print('Дешифрованная фраза:\n', sifr_ceasar(string_fail, num))
        
            


number = abs(name.get_number('Введите ключ шифрования, это целое число: '))
string_input = '''To be, or not to be, that is the question:
У лукоморья дуб зелёный;
Златая цепь на дубе том:'''
name_fail = 'file_task_04_04.txt'
write_file(string_input, name_fail, number)
read_file(name_fail, - number)
