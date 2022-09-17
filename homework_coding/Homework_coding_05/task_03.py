
# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# 1.Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# 2.Вторая — которая отфильтрует этот список следующим образом: если сумма очков 
# слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, 
# его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

from os import system
system("cls")

def select(f, col):
    return [f(x) for x in col]

def get_list(list_tuple:list)->list:
    list_output_2 = []
    for element in list_output_1:
        number = sum(select(lambda x: ord(x), element[1]))
        if number % element[0] == 0:
            list_output_2.append((number, element[1]))
    return list_output_2



list_input_1 = ['Java', 'C', 'Python', 'C++', 'Go', 'C#', 'Fortran', 'JavaScript', 'PHP', 'Scratch']
list_input_2 = [i for i in range(1, len(list_input_1) + 1)]
list_output_1 = list(zip(list_input_2, select(lambda x: x.upper(), list_input_1)))
print(list_output_1)
list_output_2 = get_list(list_output_1)
print(list_output_2)
