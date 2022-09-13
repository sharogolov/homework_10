# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.   
# Примеры:  
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90
num = [int(i) for i in input().split(', ')[:5]]
max_num = num[0]
for i in range(len(num)):
    if num[i] > max_num:
        max_num = num[i]
print(num)
print(max_num)


