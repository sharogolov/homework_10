
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
    for symbol in result:
        if symbol == '-':
            index = result.index(symbol)
            if  type(result[index - 1]) != float:
                temp = result[index + 1]
                result = result[:index] + [temp * -1] + result[index + 2:]
    return result

# def calculate(lst: list) -> float:
#     result = 0.0
#     while '*' in lst:
#         index = lst.index('*')
#         result = lst[index - 1] * lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '/' in lst:
#         index = lst.index('/')
#         result = lst[index - 1] / lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '+' in lst:
#         index = lst.index('+')
#         result = lst[index - 1] + lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '-' in lst:
#         index = lst.index('-')
#         result = lst[index - 1] - lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     return result

def calculate(lst: list) -> float:
    result = 0.0
    while ('*' or '/') in lst:
        for char in lst:
            if char == '*':
                index = lst.index('*')
                result = lst[index - 1] * lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            elif char == '/':
                index = lst.index('/')
                result = lst[index - 1] / lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]

    while ('+' or '-') in lst:
        for char in lst:
            if char == '+':
                index = lst.index('+')
                result = lst[index - 1] + lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
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


string = '10/2*5'
list_num = parse(string)
print(list_num)
list_result = bracket_opening(list_num)
result = calculate(list_result)
print(result)
