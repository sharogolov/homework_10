
# 3- Найти расстояние между двумя точками 
# пространства(числа вводятся через пробел)

# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from os import system
system("cls")

def get_point(input_string:str)->list:
    '''
    Получение координат точки
    в виде списка 
    '''
    while True:
        try:
            a = input(input_string)
            lst = list(map(int, a.split(' ')))
            return lst
        except ValueError:
            print('Это не то ...')

# a = '3 6'
# b = '2 1'
# a, b = list(map(int, a.split(' '))), list(map(int, b.split(' ')))

point_a = get_point('Введите координаты точки (числа вводятся через пробел):')
point_b = get_point('Введите координаты точки (числа вводятся через пробел):')
result = round(sum([(j - i) ** 2 for i, j in zip(point_a, point_b)]) ** 0.5, 2)
print('Расстояние между точками =', result)

