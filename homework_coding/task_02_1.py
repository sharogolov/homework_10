# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

def chek_expression():
    print('-'*24)
    print(f' X     Y     Z   result')
    print('-'*24)
    for i in(True, False):
        for j in(True, False):
            for k in(True, False):
                result = not(i or j or k) == (not i and not j and not k)
                print(i, j, k, result, sep='  ', end='\n') 

chek_expression()

