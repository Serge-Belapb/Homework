<<<<<<< HEAD
"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""

# text = " Цикл for языка Python извлекает из файлового объекта данные построчно (одну строку на каждой итерации цикла). Таким образом, количество итераций цикла определит количество строк в файле. Встроенная функция len() языка Python считает количество элементов в передаваемом в нее объекте. С ее помощью находится  количество символов в каждой строке. "
text = "Дана строка. Задача — узнать количество слов и символов, присутствующих в строке."


def count_text(texts):
    words = 0
    symbols = 0
    d = []
    for l in texts:
        words = len(text.split())
        symbols = len(text)
        sentence = text.count(".")
        d = {1:sentence, 2 : words, 3 : symbols}
    print(d)
    return (d)
    


def pri_text(k1, k2, k3):
    print("Всего предложений: ", k1)
    print("Всего слов:        ", k2)
    print("Всего символов:    ", k3)
    
    
d = count_text(text)
pri_text(*d)


=======
"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""

# text = " Цикл for языка Python извлекает из файлового объекта данные построчно (одну строку на каждой итерации цикла). Таким образом, количество итераций цикла определит количество строк в файле. Встроенная функция len() языка Python считает количество элементов в передаваемом в нее объекте. С ее помощью находится  количество символов в каждой строке. "
text = "Дана строка. Задача — узнать количество слов и символов, присутствующих в строке."


def count_text(texts):
    words = 0
    symbols = 0
    d = []
    for l in texts:
        words = len(text.split())
        symbols = len(text)
        sentence = text.count(".")
        d = {1:sentence, 2 : words, 3 : symbols}
    print(d)
    return (d)
    


def pri_text(k1, k2, k3):
    print("Всего предложений: ", k1)
    print("Всего слов:        ", k2)
    print("Всего символов:    ", k3)
    
    
d = count_text(text)
pri_text(*d)


>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
