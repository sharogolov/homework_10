# Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

from os import system
system("cls")

import function

name_fail = 'homework_05_01.txt'
name_fail_2 = 'homework_05_02.txt'
string_input = 'Сижу за решеткой в абв темнице сырой.Вскормленный абв в неволе орел абвер молодой' 


function.write_file(string_input, name_fail)
string_output = function.read_file(name_fail)
string_output = list(filter(lambda x: not 'абв' in x, string_output.split()))
string_output = ' '.join(string_output)
function.write_file(string_output, name_fail_2)