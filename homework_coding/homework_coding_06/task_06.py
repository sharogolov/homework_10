# 6-Сформировать список из N членов последовательности.
# Для 
# N = 5: 1, -3, 9, -27, 81 и т.д.

from os import system
system("cls")
import function as fun

# num = 5
num = abs(fun.get_number('Введите число для создания последовательности: '))
list_num = list((-3) ** x for x in range(num))
print(list_num)