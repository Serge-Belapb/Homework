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
import random
import string
import secrets
import calendar
import datetime
from datetime import date, timedelta


class User():
    __password = ''

    def __init__(self, name, login, password=None):
        if not password:
            password = self.genpass()
            print(f'Новый пароль - {password}')
        self._name = name
        self.login = login
        self.password = password
        self.is_blocked = False
        self.subscription_date = date.today() + timedelta(days=30)
        self.subscription_mode = 'Free'
                
    def __repr__(self):
        return f"{self.name} {self.login} {self.password}"    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def checkname(self, value):
        reg = "^[а-яА-ЯёЁ]+$"
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
        return self.__password
    
    @password.setter
    def password(self, value):
        reg = "^[a-zA-Z0-9]{0,5}$"
        if not re.match(reg, value):
            raise ValueError("Пароль должен содержать латинские буквы цифры и менее шести символов")
        self.__password = value


    def bloc(self, blocked):
        self.is_blocked = blocked
        
    def check_subscr(self, date_sub=None):
        subb = False
        if not date_sub:
            date_sub = datetime.date.today()
        else:
            date_sub = datetime.datetime.strptime(date_sub, "%Y-%m-%d").date()  
        subb = self.subscription_date> date_sub
        return (subb, self.subscription_mode, (self.subscription_date - date_sub).days)    
        # print(self.subscription_date)
        # date1 = datetime.strptime(subscription_date, '%Y-%m-%d')
        # today = date.today()
        # print(today)
        # print(date1)
        
        # if subscription_date < today:
        #     user2.bloc(self.name)
        # days = calendar.monthrange(today.year, today.month)[1]
        # new_date = today + timedelta(days=days)

    def genpass(self, password=None):
        # return re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.[A-Z])[0-9a-zA-Z]{6,}$', password)

    # def __checkpass(self, password):
    #     return re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.[A-Z])[0-9a-zA-Z]{6,}$', password)
                    
    # def change_pass(self, password=None):
        char = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(char) for i in range(5))
            # password = ''.join(random.choice(char) for i in range(5))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
                break
            self.password = password
            # print(f"Новый пароль пользователя {self.name} - {self.password}")
            return password

    def change_pass(self, passw=None):
        if not passw:
            passw = self.genpass()
            print(f"Новый пароль пользователя {self.name} - {passw}")


    def get_info(self):
        name = self.name
        login = self.login
        password = self.password

        return name, login, password

    def save(self):
        pass




class Users:
    def __init__(self) -> None:
        pass




# print(d_txt)    
dat = '2024-1-1'
 
# is_blocked = []
# subscription_date = date.today().year
# subscription_mode = 1  # free  paid
    
user1 = User('Иванов', 'Ivan_v', 'lbP17')
user2 = User('Петро', 'Petr_v', 'EDgt3')

print(user1._name, user1.login)
# print(check_subscr(dat))
print(user1.get_info())
print(user2.get_info())
user1.password = 'JuK12'
user1.change_pass()
print(user1.get_info())
user2.check_subscr()