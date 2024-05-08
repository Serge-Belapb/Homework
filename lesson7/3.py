<<<<<<< HEAD
'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

chislo = input("Введите число: ")
print(len(chislo))
print(chislo)
print(chislo[0])
d = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h",
    9:"i",
    0:"j"
}
ch_b = []
i = 0
dn = dict()
if d[i] == chislo[i]:
    d1 = {key:d[key] for key in d}


print(d1)

for key in d:
    if key == chislo[i]:
        print(chislo[i])
        dn.append(d[key])
        print(dn)
        i += 1

d1 = {key:key for key in d}

            # print(chislo[i])
            # ch_b += ch_b.append(list(d[key]))
            # i += 1
    
            # print(ch_b)

# создаем словарь из списка
# d = {num+num:num**num for num in nums}
=======
'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

chislo = input("Введите число: ")
print(len(chislo))
print(chislo)
print(chislo[0])
d = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h",
    9:"i",
    0:"j"
}
ch_b = []
i = 0
dn = dict()
if d[i] == chislo[i]:
    d1 = {key:d[key] for key in d}


print(d1)

for key in d:
    if key == chislo[i]:
        print(chislo[i])
        dn.append(d[key])
        print(dn)
        i += 1

d1 = {key:key for key in d}

            # print(chislo[i])
            # ch_b += ch_b.append(list(d[key]))
            # i += 1
    
            # print(ch_b)

# создаем словарь из списка
# d = {num+num:num**num for num in nums}
>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
# print(d)