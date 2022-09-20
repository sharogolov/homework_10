# 6-Сформировать список из N членов последовательности.
# Для 
# N = 5: 1, -3, 9, -27, 81 и т.д.

from os import system
system("cls")

num = 5
list_num = list((-3) ** x for x in range(num))
print(list_num)