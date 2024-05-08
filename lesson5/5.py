<<<<<<< HEAD
a = input('Введите фразу: ')
b = len(a)
c = []
i = 0
while i < b:
    c.append(a[i])
    i += 1
print("Количество уникальных символов ", len(set(c)))

l = a.lower().split()
d = []
for i in l:
    if i not in d:
        d.append(i)
print("Количество уникальных слов ", len(d))




=======
a = input('Введите фразу: ')
b = len(a)
c = []
i = 0
while i < b:
    c.append(a[i])
    i += 1
print("Количество уникальных символов ", len(set(c)))

l = a.lower().split()
d = []
for i in l:
    if i not in d:
        d.append(i)
print("Количество уникальных слов ", len(d))




>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
