"""
Создать класс Student.

Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

class Student:
    grads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
    def __init__(self, surname, name, group):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = []

    def __eq__(self, obj) -> bool:
        self.av_gr == obj.av_gr
    def __ne__(self, obj: object) -> bool:
        pass
    def __lt__(self, obj: object) -> bool:
        pass
    def __gt__(self, obj: object) -> bool:
        pass
    def __le__(self, obj: object) -> bool:
        pass
    def __ge__(self, obj: object) -> bool:
        pass    

    def __repr__(self):
        return f"{self.surname} {self.name} ({self.group})"
    
class Students:
    lst = []
    grads = []

    @staticmethod
    def add(student):
        Students.lst.append(student)
        
    @staticmethod
    def sort():
        Students.lst.sort(key=lambda s: s.surname)
    
    @staticmethod
    def resort():
        Students.lst.sort(key=lambda s: s.surname, reverse=True)
    
    @staticmethod
    def add_grade(self, *grads):
        Students.grads.append(grads)
    
    @staticmethod
    def average_grade(self, av_gr):
        av_gr = sum(self.grads) % len(self.grads)
        return av_gr

 
st_1 = Student("Иванов", "Иван", 222)
st_2 = Student("Петров", "Петр", 218)
st_3 = Student("Сидоров", "Андрей", 219)
st_4 = Student("Харламов", "Валерий", 217)
st_5 = Student("Гагарин", "Юрий", 215)
print(Students.lst)
Students.add(st_1)
Students.add(st_2)
Students.add(st_3)
Students.add(st_4)
Students.add(st_5)
print(Students.lst)
Students.sort()
print(Students.lst)
Students.resort()
print(Students.lst)


# Students.average_grade()
Students.add_grade(5, 2, 3, 4, 9)
print(Students.grads)
Students.average_grade()
print(Students.grads)