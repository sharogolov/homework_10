# Найти сумму элементов массива, лежащих между максимальным
#  и минимальным по значению элементами
# [1,8,16,3,5,9,4]
# 1+8+16 = 25

list_number = [1,8,16,3,5,9,4]
index_min = list_number.index(min(list_number))
index_max = list_number.index(max(list_number))
if index_max >index_min:
    result =  sum(list_number[index_min:index_max + 1])  
else:
     result =  sum(list_number[index_max:index_min + 1])
print(result) 