# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

number = [int(i) for i in input('Введите 3 числа через запятую: ').split(',')]
expression_1 = not(number[0] or number[1] or number[2])
expression_2 = not number[0] or not number[1] or not number[2]
result = expression_1 == expression_2
if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')