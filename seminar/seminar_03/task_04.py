
# В текстовом файле посчитать количество строк, 
# а также для каждой отдельной строки определить 
# количество в ней символов и слов.

f = open('article.txt','r')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(len(i), 'симв.', word, 'сл.')
print(line, 'стр.')
f.close()
