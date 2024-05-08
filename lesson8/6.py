<<<<<<< HEAD
"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

sp = [1, 2, 1, 3, 1, 4]


def yes_or_no(spisok):
    s = spisok
    n = 'no'
    y = 'yes'
    spi = []
    for i in s:
        b = spisok.count(i)
        if b == 1:
            spi.append(n)
        else:
            spi.append(y)
    return(spi)

        
=======
"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

sp = [1, 2, 1, 3, 1, 4]


def yes_or_no(spisok):
    s = spisok
    n = 'no'
    y = 'yes'
    spi = []
    for i in s:
        b = spisok.count(i)
        if b == 1:
            spi.append(n)
        else:
            spi.append(y)
    return(spi)

        
>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
print(yes_or_no(sp))