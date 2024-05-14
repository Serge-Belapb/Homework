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
        {"name":"some_name3", "login":"some_login3", "password":"pass" },
]

spis_pass = filter(lambda x : True if len(x['password']) < 5 else False, spis)
print(list(spis_pass))









# l = [[1, 2, 9, [2]], [1, 9, 4, [6]], [2, 9, 3, [6]]]
# l3 = filter(lambda x:True if x[2]==9 else False, l)
# print(list(l3))