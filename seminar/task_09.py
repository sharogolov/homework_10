# Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

# string_1 = input()
# string_2 = input()
# if string_1 > string_2:
#     print(string_1.count(string_2))
# else:
#     print(string_2.count(string_1))


# string_1 = input()
# string_2 = input()
# count = 0
# if string_1 > string_2:
#     while string_2 in string_1:
#         string_1 = string_1[string_1.find(string_2):]
#         count += 1
# if string_2 > string_1:
#     while string_1 in string_2:
#         string_2 = string_2[string_2.find(string_1):]
#         count += 1
# print(count)

a = 'pyt'
b = 'pythonpythonpython'
count = 0
for i in range(0, len(b) - len(a)):
    if b[i:i + len(a)] == a:
        count += 1 
print(count)