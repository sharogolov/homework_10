# Найдите количество элементов массива, которые отличны
#  от наибольшего элемента не более чем на 10%.

list_number = [1,8,7,10,5,9,4]
count = 0
max_num = max(list_number)
number_10 = max_num * 0.1

for i in list_number:
    if i != max_num:
        if (max_num - i) <= number_10:
            count += 1 

print(count)


# list_number = [1,8,7,10,5,9,4]
# count = 0
# max_num = max(list_number)
# #number_10 = max_num * 0.1

# for i in list_number:
#     if i != max_num:
#         if max_num - i <= i * 0.1:
#             count += 1 

# print(count)