<<<<<<< HEAD
'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

fraza = input("Введите фразу состоящую минимум из трех слов: ").split()
kol = len(fraza)
print(kol)
k = 0
x = ""
i = 0
y = 0
while k <= kol and y == kol:
    for i in fraza[y]:
        x = x + i
        y += 1
        print(x)
        print(y)

# def kol_bukv:
#     r = ""
#     s = input()
#         for i in range(1, len(s) + 1):
#         r += s[i - 1] * i
#     return r
#     print(r)


=======
'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

fraza = input("Введите фразу состоящую минимум из трех слов: ").split()
kol = len(fraza)
print(kol)
k = 0
x = ""
i = 0
y = 0
while k <= kol and y == kol:
    for i in fraza[y]:
        x = x + i
        y += 1
        print(x)
        print(y)

# def kol_bukv:
#     r = ""
#     s = input()
#         for i in range(1, len(s) + 1):
#         r += s[i - 1] * i
#     return r
#     print(r)


>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
