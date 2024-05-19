"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args: int, **kwargs: str):
    print(args, kwargs)
    di ={}
    try:
        args_sum = sum(args)
        print("args_sum :", args_sum)
    except TypeError:
        args_sum = "Все позиционные аргументы должны быть целыми"
        print(args_sum)   
    try: 
        max_val = max(kwargs.values())
        fin_dict = list(len(v) for k, v in kwargs.items() if v == max_val)
        print("kwargs_max_len :", fin_dict)
    except TypeError:
        kwargs_max_len = "Все аргументы - ключевые слова должны быть строками"
        print(kwargs_max_len)
    di = {"args_sum" : args_sum, "kwargs_max_len" : fin_dict}    
    return di
    

print(dict_from_args(1, 2, 3, 4, q='world', w='Hello'))