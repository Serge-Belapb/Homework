"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""


class Animal():
    name: str
    def __init__(self, name):
        self.name = name
         
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    def say(self):
        return (f"{self.name} - кошка. Говорит МЯУ!")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    def say(self):
        return (f"{self.name} - собака. Говорит ГАВ!")

class Cow(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    def say(self):
        return (f"{self.name} - корова. Говорит МУ!")
 


myCat = Cat("Tom")
myDog = Dog("Бим")
myCow = Cow("Березка")

print(myCat.say())
print(myDog.say())
print(myCow.say())