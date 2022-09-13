# Напишите программу, которая определит 
# позицию второго вхождения строки в списке либо 
# сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], 
# ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], 
# ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], 
# ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", 
# ответ: -1
# - список: [], ищем: "123", ответ: -1


# list_string = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

# index = list_string.index('qwe')
# index_2 = list_string[index + 1:].index('qwe') + index + 1 
# #print(list_string[index:])
# print(index_2)

# list_string = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

# index = list_string.index('йцу')
# index_2 = list_string[index + 1:].index('йцу') + index + 1 
# #print(list_string[index:])
# print(index_2)

spisok = ['строка1', 'строка2', 'строка3', 'строка1']
find_str = 'строка1'
if spisok.count(find_str) < 2:
    print(f'Второго вхождения строки {find_str} нет в заданном списке')
else:
    spisok1 = spisok[spisok.index(find_str) + 1:] # отрезаем первой вхождение
    print(spisok1.index(find_str) + (len(spisok) - len(spisok1))) # ищем строку в оставшемся списке и прибавляем то количество элементов, которое отрезали
