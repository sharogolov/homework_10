# Задайте два числа. Напишите программу, 
# которая найдет НОК (наименьшее общее кратное) этих двух 
# чисел. НОК - наименьшее общее кратное, которое делится и на 
# первое, и на второе число. 

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
#flag = True
#while flag == True:
if num_1 > num_2:
    num_1, num_2 = num_2, num_1
for i in range(1, num_2 + 1):
    if (num_1 * i) % num_2 == 0:
        print('НОК', num_1 * i)
        #
        #flag = False
        break

        