<<<<<<< HEAD
s1 = ['a', 'b', 'c' ,'d']
s2 = [10, 20, 30, 40]
sl = dict(zip(s1, s2))
print(sl)
a = input('Кодовая фраза: ')
b = int(len(a))
d = 0
i = 0                      
while i < b:         
    d = d + sl.get(a[i])    
    i += 1 
print('Сумма очков: ', d)
=======
s1 = ['a', 'b', 'c' ,'d']
s2 = [10, 20, 30, 40]
sl = dict(zip(s1, s2))
print(sl)
a = input('Кодовая фраза: ')
b = int(len(a))
d = 0
i = 0                      
while i < b:         
    d = d + sl.get(a[i])    
    i += 1 
print('Сумма очков: ', d)
>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
