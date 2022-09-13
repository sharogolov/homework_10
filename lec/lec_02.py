
from fileinput import close


# colors = ['red', 'green', 'blue123']
# data = open('file2.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# # еще конструкция для записи
# with open('fail2.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


path = 'file2.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
