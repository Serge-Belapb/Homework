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
import datetime
import random
import string
import secrets
import calendar
from datetime import date, timedelta
from datetime import datetime


class User:
    def __init__(self, name, login, password, *subscription_date, **subscription_mode):
        self._name = name
        self.login = login
        self.password = password
        self.is_blocked = []
        self.subscription_date = subscription_date
                
    def __repr__(self):
        return f"{self.name} {self.login} ({self.password})"    

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
        return self._password
    
    @password.setter
    def password(self, value):
        reg = "^[a-zA-Z0-9]{0,5}$"
        if not re.match(reg, value):
            raise ValueError("Пароль должен содержать латинские буквы цифры и менее шести символов")
        self._password = value


    def bloc(self, name):
        self.is_blocked.append(name)
        with open("block.txt", "w") as file:
            print(*self.is_blocked, file=file)
	

    def check_subscr(self, *subscription_date):
        print(subscription_date)
        # date1 = datetime.strptime(subscription_date, '%Y-%m-%d')
        today = date.today()
        print(today)
        # print(date1)
        
        # if subscription_date < today:
        #     user2.bloc(self.name)
        days = calendar.monthrange(today.year, today.month)[1]
        new_date = today + timedelta(days=days)
                
        print(new_date)
        return new_date
    
    
    def change_pass(self, *password):
        char = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(char) for i in range(5))
            # password = ''.join(random.choice(char) for i in range(5))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
                break
            self.password = password
            print(f"Новый пароль пользователя {self.name} - {self.password}")
            return password

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
user2 = User('Петров', 'Petr_v', 'EDgt3', dat)

print(user1._name, user1.login)
# print(check_subscr(dat))
print(user1.get_info())
user1.change_pass()
print(user1.get_info())
user2.check_subscr()