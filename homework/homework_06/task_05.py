# Напишите программу вычисления арифметического выражения 
# заданного строкой.
# Используйте операции +,-,/,*. приоритет операций 
# стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих 
# приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

from os import system
system("cls")

def parse(s: str)-> list:
    result = []
    digit = ''
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symbol)
    if digit:
        result.append(float(digit))
    temp_lst = [y for x, y in zip(result, list(range(len(result)))) if x == '-']
    print(temp_lst)
    for i in temp_lst:
        if type (result[i - 1]) != float:
            temp = result[ i + 1]
            result = result[:i] + [temp * -1] + result[i + 2:]        
    return result

def calculate(lst: list) -> float:
    result = 0.0
    for char in lst:
        if char == '*':
            index = lst.index('*')
            result = lst[index - 1] * lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
        elif char == '/':
            index = lst.index('/')
            result = lst[index - 1] / lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    for char in lst:
        if char == '+':
            index = lst.index('+')
            result = lst[index - 1] + lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
        elif char == '-' :
            index = lst.index('-')
            result = lst[index - 1] - lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

def bracket_opening(lst: list) -> list:
    while '(' in lst:
        close = lst.index(')')
        temp_lst = [y for x, y in zip(lst[:close], list(range(close-1))) if x == '(']
        open = temp_lst[-1]        
        lst = lst[:open] + [calculate(lst[open + 1: close])] + lst[close + 1:]
    return lst    


string = '(2+((5-3)*(16-14)))/-3'
list_num = parse(string)
print(list_num)
list_result = bracket_opening(list_num)
result = calculate(list_result)
print(result)
