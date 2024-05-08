<<<<<<< HEAD
'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
stroka = "hxtrhth srhxrxhx "
s = set(stroka)


def find_dubl(str):
    s = set(str)
    new_dict = []
    for i in s:
        b = str.count(i)
        new_dict.append(f'{i}:{b}')
    return new_dict 


print(find_dubl(stroka))

=======
'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
stroka = "hxtrhth srhxrxhx "
s = set(stroka)


def find_dubl(str):
    s = set(str)
    new_dict = []
    for i in s:
        b = str.count(i)
        new_dict.append(f'{i}:{b}')
    return new_dict 


print(find_dubl(stroka))

>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
