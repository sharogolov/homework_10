# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.

try:
    def sum_number(number):
        number = int(number)
        list_number = []
        if number > 0:
            for i in range(1, number + 1):
                list_number.append((1 + 1 / i) ** i)
        else:
            for i in range(number, 0, -1):
                list_number.append((1 + 1 / i) ** i)
        return round(sum(list_number), 2)

    
    num = input('Введите число: ')
    result = sum_number(num)
    print(result)
except(ValueError):
    print('Что-то пошло не так...')
