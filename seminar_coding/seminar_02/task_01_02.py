# Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов. 
#     *Пример:*    
#     - Для N = 5: 1, -3, 9, -27, 81

def number():
    #while True:
    try:
        num = int(input('Введите число: '))
        return num
    except(ValueError):
        print('Вы ввели не число')
        return number()

number_n = number() 

for i in range(number_n):
    print((-3) ** i, end=', ')
