<<<<<<< HEAD
a = input('Числа через пробел 1: ')
b = input('Числа через пробел 2: ')
c = input('Числа через пробел 3: ')
w = a.split() + b.split() + c.split()
d = set(w)
print(sorted(d))

ww = list(set(a.split()) & set(b) & set(c))
=======
a = input('Числа через пробел 1: ')
b = input('Числа через пробел 2: ')
c = input('Числа через пробел 3: ')
w = a.split() + b.split() + c.split()
d = set(w)
print(sorted(d))

ww = list(set(a.split()) & set(b) & set(c))
>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
print(ww)