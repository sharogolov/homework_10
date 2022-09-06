# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: 
# "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны
#  читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются
#  на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного 
# пользователем числа.
    
def get_number():
    try:
        num = int(input('Введите число: '))
        return num
    except(ValueError):
        return get_number()

def palindrom(num):
    if int(num) < 0:
        return print('Палиндром для отрицательного числа не существует')
    elif num != num[::-1]:
        num = str(int(num) + int(num[::-1]))
        return palindrom(num)
    else:
        #result = num
        return print(f'Палиндром = {num}')

number = str(get_number())
palindrom(number)
#print(f'Палиндром для числа {number} = {number_result}')