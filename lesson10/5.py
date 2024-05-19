"""
Написать генератор последовательности Фибоначчи, 
который принимает максимальное количество чисел в последовательности из чисел Фибоначчи 
и генерирует последовательность. 
Затем  вывести на экран элементы данного генератора. 
Фибоначчи последовательность - первые два числа которой являются 0 и 1, 
а каждое последующее за ними число является суммой двух предыдущих. 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и так далее.  
"""

def fiba(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fiba(11)))  





n = int(input("Введите число: "))
a, b = 0, 1
while b <= n:
    a, b = b, a + b
    print(a)