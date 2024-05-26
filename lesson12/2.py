"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year
print(CURRENT_YEAR)

class BookCard():
    author: str
    title: str
    year: int

    def __init__(self, author, title, year) -> None:
        self.author = author
        self.title = title
        self.year = year
        
    def __le__(self, obj):
        return self.year <= CURRENT_YEAR
    
    @property  # геттер
    def year(self):
        return self.year
    
    @year.setter
    def year(self, val):
        if self.__le__(val) is isinstance(val, int):
            self.year = val
        else:
            ValueError ("Не тот тип данных")



books = [
    BookCard("Автор1", "Ноутбук", 2000),
    BookCard("Автор2", "Телефон", 2005),
    BookCard("Автор3", "Компьютер", 2019),
         
]