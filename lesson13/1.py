"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. 
Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, 
и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""

import re
from datetime import datetime
import random


class User:
    def __init__(self, name, login, password, is_blocked):
        self._name = name
        self.login = login
        self.password = password
        self.is_blocked = True

    def __repr__(self):
        return f"{self.name} {self.login} ({self.password})"    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def checkname(self, value):
        reg = "^[а-яА-ЯёЁ]$"
        if not re.match(reg, value):
            raise ValueError("Имя должно содержать только буквы русского алфавита")
        self._name = value
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, value):
        reg = r"^[a-zA-Z0-9-_\.]{5,20}$"
        if not re.match(reg, value):
            raise ValueError("Логин должен содержать латинские буквы цифры и черту подчеркивания быть не менее 6 символов")
        self._login = value
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        reg = "^[a-zA-Z0-9]{0,5}$"
        if not re.match(reg, value):
            raise ValueError("Пароль должен содержать латинские буквы цифры и менее шести символов")
        self._password = value


    # def is_blocked():
    #     pass
    
    is_blocked = []

    def bloc(func):
        @wrapper(func)
	    def decorator(mes):
		    if mes not in is_blocked:
			    return func(mes)
            else:
                is_blocked.append(mes)
	    return decorator
        
       

    def check_subscr(self, dt):
        return datetime(*dt).date
    
   
    def change_pass(self, *password):
        if not password:
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            chars1 = 'abcdefghijklnopqrstuvwxyz'
            chars2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            chars3 = '1234567890'
            length = 5
            password =''
            for i in range(length-3):
                    password += random.choice(chars)
            password += random.choice(chars1)
            password += random.choice(chars2)
            password += random.choice(chars3)
        print(password)
        return self.password

    def get_info()

# print(d_txt)    
dat = (2024, 1, 12)
 
# is_blocked = []
# subscription_date = date.today().year
# subscription_mode = 1  # free  paid
    
user1 = User('дмдшрм', 'knk_v', 'lbP7')

print(user1._name, user1.login)
# print(check_subscr(dat))
user1.change_pass('GGl8')
user1.change_pass()
print(user1.password)