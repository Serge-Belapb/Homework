'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''

sp = [1,2,3,4,5,6,7,8,9]
new_sp1 = sp.copy()
new_sp2 = sp.copy()
new_sp3 = sp.copy()


sq_fun = lambda x: x * x
print(list(map(sq_fun, new_sp1)))


plus3_fun = lambda x: x + 3 if x % 2==0 else x
print(list(map(plus3_fun, new_sp2)))


umno_fun = lambda x: x * 2 if x % 2==0 else x * 3
print(list(map(umno_fun, new_sp3)))