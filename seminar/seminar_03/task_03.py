# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка
# и возвращает словарь, в котором каждый элемент списка является и ключом
# и значением. Предполагается, что элементы списка будут соответствовать
# правилам задания ключей в словарях.
# # Тесты
# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))

list_string = [1, 2, 3, 4]
list_string_2 = ['grey', (2, 17), 3.11, -4]


def to_dict(list_string):
    return{element: element for element in list_string}
    

print(to_dict(list_string))
print(to_dict(list_string_2))
