"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""

def log_decorator(fun_to_decor):
    def wrapper(arg):
        print(f"Выполняеся функция <hello> с аргументами {arg}")
        fun_to_decor(arg)
        print(f"Функция <hello> - завершена")
    return wrapper
 
# Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
# передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
@log_decorator
def hello(name):
    print(f"Привет, {name}")

hello("Vasya")