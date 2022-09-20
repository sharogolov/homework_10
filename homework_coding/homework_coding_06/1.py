
s = '(2+((5-3)*(16-14)))/-3'
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
print(result)