"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""
def bread(fun_to_dekor):
    def wrapper():
        print("</------------\\>")
        fun_to_dekor()
        print("<\\____________/>")
    return wrapper

def onion(fun_to_dekor):
    def wrapper():
        print("----- лук ------")
        fun_to_dekor()
    return wrapper

def tomato(fun_to_dekor):
    def wrapper():
        print("*** помидоры ****")
        fun_to_dekor()
        
    return wrapper

def salad(fun_to_dekor):
    def wrapper():
        print("~~~~ салат ~~~~~")
        fun_to_dekor()
    return wrapper

def cheese(fun_to_dekor):
    def wrapper():
        print("^^^^^ сыр ^^^^^^")
        fun_to_dekor()
    return wrapper

def beef():
    print("### говядина ###")

def chicken():
    print("|||| курица ||||")


gamburger = bread(onion(tomato(beef)))
gamburger()

chickenburger = bread(cheese(salad((chicken))))
chickenburger()



