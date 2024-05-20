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
    di ={}
    try:
        args_sum = sum(args)
    except TypeError:
        print("Все позиционные аргументы должны быть целыми")   
    try: 
        
        max_val = max(list(kwargs.values()), key=len)
    except TypeError:
        print("Все аргументы - ключевые слова должны быть строками")
    di = {"args_sum" : args_sum, "kwargs_max_len" : len(max_val)}    
    return di
    

import json
print(json.dumps(dict_from_args(1, 1, 3, 4, q='wooooooorlds', w='Helloss'), indent=4, sort_keys=True))

