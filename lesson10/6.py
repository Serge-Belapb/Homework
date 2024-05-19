"""
Написать функцию счетчик которая с помощью замыкания 
будет хранить в себе количество запускови каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""

def out_function():
    n = 10
    def in_function():
        nonlocal n
        n +=1
        return n
    return in_function

c1 = out_function()
print(c1())
print(c1())
print(c1())
print(c1())


