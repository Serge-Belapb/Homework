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

class BookCard:
    def __init__(self, author, title, year):
        self.__author = author    
        self.__title = title      
        self.__year = year       
                  
    def print_info(self):
        print(f"Автор: {self.__author}\tНазвание: {self.__title}\tГод издания: {self.__year}")

    def __le__(self, obj):
        return self.year <= CURRENT_YEAR

    def __repr__(self):
        return f"{self.__author} {self.__title} ({self.__year})"

    @property  # геттер
    def author(self):
        return self.__author
    @property  
    def title(self):
        return self.__title
    @property 
    def year(self):
        return self.__year
    
    @author.setter
    def author(self, other):
        if self.author is isinstance(other, str):
            self.author = other
        else:
            ValueError ("Не тот тип данных")
        return self.author
    
    @title.setter
    def title(self, other):
        if self.title is isinstance(other, str):
            self.title = other
        else:
            ValueError ("Не тот тип данных")
        return self.title
    
    @year.setter
    def year(self, ye):
        if 0 < ye <= CURRENT_YEAR is isinstance(ye, int):
            self.year = ye
        else:
            ValueError ("Не тот тип данных")




class Books:
    lst = []
    
    @staticmethod
    def add(book):
        Books.lst.append(book)
        
    @staticmethod
    def sort():
        Books.lst.sort(key=lambda s: s.year)



book1 = BookCard("Автор1", "Ноутбук", 2000)
book2 = BookCard("Автор2", "Телефон", 1995)
book3 = BookCard("Автор3", "Компьютер", 1991)
book1.print_info()

print(Books.lst)
Books.add(book1)
Books.add(book2)
Books.add(book3)
print(Books.lst)

Books.sort()
print(Books.lst)
    



# books = [
#     BookCard("Автор1", "Ноутбук", 2000),
#     BookCard("Автор2", "Телефон", 2005),
#     BookCard("Автор3", "Компьютер", 2019),
         
# ]

