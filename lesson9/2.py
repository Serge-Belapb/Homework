'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''


n = 1


def printn(text):
    global n
    for i in text:
        print(n, text)
        n += 1
    return   


print(printn(input("  :")))