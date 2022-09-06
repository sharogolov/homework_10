# Сортировка пузырьком

list_num = [1,8,7,10,5,9,4]
n = len(list_num)
for i in range(n - 1):
    for j in range(n - i - 1):
        if list_num[j] > list_num[j + 1]:
            list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j] 
print(list_num)



