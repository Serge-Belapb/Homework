'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''

a = int(input("Целое число1 :"))
b = int(input("Целое число2 :"))

# sp = list(range(a, b+1))
# print(sp)
# for i in sp:
#     rez = sum(sp)
# print(rez)


def summab(d1, d2):
    sp = list(range(d1, d2+1))
    for i in sp:
        rez = sum(sp)
    return rez  


print(f"Сумма всех чисел от {a} до {b} :", summab(a,b))