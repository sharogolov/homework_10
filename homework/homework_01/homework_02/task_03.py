# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.

def get_number():
    try:
        num = int(input('Введите число: '))
        return num
    except(ValueError):
        return get_number()


def sum_number(number):
    number = int(number)
    if number == 0:
        return 'Последовательность из нуля чисел равна нулю'
    if number < 0:
        return 'Последовательность не может быть отрицательной'
    list_number = list((1 + 1 / i) ** i for i in range(1, number + 1))
    return round(sum(list_number), 2)

    
num = get_number()
result = sum_number(num)
print(result)

