# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

try:
    def count_number(number):
        number_list =[]
        j = 0
        for i in number:
            if i != '.':
                number_list.append(i)
                number_list[j] = int(number_list[j])
                j += 1
        return sum(number_list)
    
    num = input('Введите число: ')
    result = count_number(num)
    print(result)
    
except(ValueError):
    print('Что-то пошло не так...')