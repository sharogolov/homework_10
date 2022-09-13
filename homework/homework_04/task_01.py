# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    10^{-1} ≤ d ≤10^{-10}

from os import system
system("cls")

def сalculation_number(num:float, degree:str)->float:
    '''
    Округление числа с заданной точностью
    '''
    return round(num, len(degree) - 2)

number = input('Введите необходимую точность округления (например 0.001): ')
num_round = float(input('Введите число для округления: '))
result = сalculation_number(num_round, number)
print(f'Число с точностью {len(number) - 2} знаков после запятой = {result}')
