<<<<<<< HEAD
#  Даны 4 переменные - a1, a2, a3, a4.
a1 = 5.2
a2 = 5.3
a3 = 4.7
a4 = 3.3

d1 = isinstance(a1, float)
d2 = isinstance(a2, float)
d3 = isinstance(a3, float)
d4 = isinstance(a4, float)
if d1 == True and d2 == True and d3 == True and d4 == True:
    print("True")
else: 
    print("False")

b1 = isinstance(a1, str)
b2 = isinstance(a2, str)
if b1 == True or b2 == True:
    print("True")
else: 
    print("False")

#  a1-a3, a2-a4, a3-a4
e1 = a1-a3
e2 = a2-a4
e3 = a3-a4
print(e1)
print(e2)
print(e3)
c1 = isinstance(e1, int)
c2 = isinstance(e2, int)
c3 = isinstance(e3, int)
if c1 == True or c2 == True or c3 == True:
    print("True")
else: 
=======
#  Даны 4 переменные - a1, a2, a3, a4.
a1 = 5.2
a2 = 5.3
a3 = 4.7
a4 = 3.3

d1 = isinstance(a1, float)
d2 = isinstance(a2, float)
d3 = isinstance(a3, float)
d4 = isinstance(a4, float)
if d1 == True and d2 == True and d3 == True and d4 == True:
    print("True")
else: 
    print("False")

b1 = isinstance(a1, str)
b2 = isinstance(a2, str)
if b1 == True or b2 == True:
    print("True")
else: 
    print("False")

#  a1-a3, a2-a4, a3-a4
e1 = a1-a3
e2 = a2-a4
e3 = a3-a4
print(e1)
print(e2)
print(e3)
c1 = isinstance(e1, int)
c2 = isinstance(e2, int)
c3 = isinstance(e3, int)
if c1 == True or c2 == True or c3 == True:
    print("True")
else: 
>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
    print("False")