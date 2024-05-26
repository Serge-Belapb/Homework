"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:
    def __init__(self, brand, model, issue_year) -> None:
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f"{self.brand}-{self.model} - Звонит {name}")

    def get_info(self):
        brand = self.brand
        model = self.model
        issue_year = self.issue_year
        return brand, model, issue_year

    def __str__(self) -> str:
        print(
              f"Бренд:       {self.brand}\n" \
              f"Модель:      {self.model}\n" \
              f"Год выпуска: {self.issue_year}\n"
        )


ph1 = Phone("Nokia", 6610, 1998)
ph2 = Phone("Xiaomi", 10, 2018)

ph1.receive_call("Dima")
ph2.receive_call("Ivan")

print(ph1.get_info())
print(ph2.get_info())

ph1.__str__()
ph2.__str__()