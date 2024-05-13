'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''
n = int(input("Введите число: "))


def factorial(n):
    if n <= 1:
        return 1
    else:
        return (n * factorial(n-1))


print(f"Факториал числа {n} равен:", factorial(n))
