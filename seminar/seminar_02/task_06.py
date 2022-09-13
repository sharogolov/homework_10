def search_anton(number):
    list = []
    for i in range(len(number)):
        count = 0
        if 'a' in number[i].lower():
            count += 1
        if 'n' in number[i].lower():
            if number[i].count('n') >= 2:
                count += 1
        if 't' in number[i].lower():
            count += 1
        if 'o' in number[i].lower():
            count += 1
        if count == 4:
            list.append(i + 1)
    return list



num = int(input())
string = []
for i in range(num):
    string.append(input())
print(string)
result = search_anton(string)
print(result)



# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)                   
# print(*list1)

