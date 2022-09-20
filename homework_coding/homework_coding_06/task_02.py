# 2- Найти сумму чисел списка стоящих 
# на нечетной позиции

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
# ответ: 12
from os import system
system("cls")

list_1 = [2, 3, 5, 9, 3]
result = sum([v for i, v in enumerate(list_1) if i % 2])
print(result)
