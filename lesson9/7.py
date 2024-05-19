"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""

spis = [{"name":"some_name", "login":"some_login", "password":"some_password" },
        {"name":"some_name2", "login":"some_login2", "password":"som_password" },
        {"name":"some_name3", "login":"some_login-3", "password":"pass" },
]

spis_pass = filter(lambda x : True if len(x['password']) < 5 else False, spis)
print(list(spis_pass))

import string

great_sym = string.ascii_letters + string.digits + '_'
print(great_sym)


def fil_valid(spis):
    for s in spis['login']:
        if not s in great_sym:
            return False
    return True
   
lnv = list(filter(fil_valid, spis))
print(lnv)

lnv = list(filter(
           lambda x :
             any(map(lambda x : not x in great_sym, x['login'])), spis))
print(lnv)
