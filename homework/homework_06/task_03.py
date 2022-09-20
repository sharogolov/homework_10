
# 2- Найти сумму чисел списка стоящих 
# на нечетной позиции

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
# ответ: 12

from os import system
system("cls")

import function as fun

# list_1 = [2, 3, 5, 9, 3]
number = abs(fun.get_number('Введите размер списка, это должно быть целое число: '))
list_1 = fun.get_list(number)
result = sum([v for i, v in enumerate(list_1) if i % 2])
print('Список элементов:\n', list_1)
print('Сумма элементов стоящих на нечетных позициях =', result)