"""
в файле hero1 добавить следующий функционал
        - добавить несколько классов других героев унаследовав их от Hero.
        - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
                и свойство отражающее урон от спец.атаки.
        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод atack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод choose_warrior, который не принимает аргументов и возвращает случайного
                воина из warriors
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle.
                
                
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.

"""

import random


class Spell:
    def __init__(self, name, dang=10, mana=5, type=1) -> None:
        self.name = name

class Hero:
    """     
    Класс дял создания героя 
    
     ...

    Attributes
    ----------
    name : str
        Имя героя
    health : int
        здоровье героя 
    age : int
        age of the person

    Methods
    -------
    print_info():
        Печатает в консоль информацию о герое
    
    kick():
        производит один удар - высчитывает и уменьшает броню и здоровье 
    
    """
    #  свойства класса - каждый созданный объект будет их иметь по умолчанию
    option1 = True
    points = 0
    level = 1

    # конструктор - тут мы создаем свойства которые должны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    def __init__(self, name, health, armor, strong) -> None:
        # свойства объектов
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
    
    # методы - это действия/команды которые могут выполнять объекты
    def _get_info(self):
        print(
              f"Имя {self.name}\n" \
              f"Здоровье - {self.health}\n" \
              f"Защита {self.armor}"
        )
        
    def print_info(self):
        
        print(self._get_info(), '\n')
    
    def kick(self, other):        
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0
            
    def special_attack(self, other):
        other.armor -= (self.strong + self.spells)
        if other.mana > 5 and other.armor < 0:
            other.health += other.armor
            other.armor = 0


class Mag(Hero):    
    def __init__(self, name, health, armor, strong, mana, spells) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        super().__init__(name, health, armor, strong)
        self.mana = mana
        self.spells = spells
        self.base_spell = fireball
        


    def cast_spell(self):
        print(self.base_spell)
    

    def print_info(self, sep="-"):
        info =  f"{super()._get_info()}\n"  \
                f"{sep*20}\n" \
                f"Мана - {self.mana}\n"
        print(info)


class Knight(Hero):
    def __init__(self, name, health, armor, strong ) -> None:
        super().__init__(name, health, armor, strong)


class Archer(Hero):
    def __init__(self, name, health, armor, strong, mana, skin, spells) -> None:
        super().__init__(name, health, armor, strong)
        self.mana = mana
        self.spells = spells
        self.base_spell = firebolt
        self.skin = skin

    def print_info(self, sep="-"):
        info =  f"{sep*50}\n" \
                f"{super()._get_info()}\n"  \
                f"{sep*20}\n" \
                f"Мана - {self.mana}\n"  \
                f"Броня - {self.skin}\n"  \
                f"Спец навык - {self.base_spell.name}"
        print(info)    
    
    # def special_attack(self, other):
    #     other.armor -= (self.strong + self.spells)
    #     if other.mana > 5 and other.armor < 0:
    #         other.health += other.armor
    #         other.armor = 0

    def attack(self, other):
        r = random.randint(1, 100)
        if r >= 75:
            other.kick()
            print(f'Тип атаки - обычная, твой шанс: {r}') 
        elif r <= 25:
            other.special_attack()
            print(f'Тип атаки - специальная, твой шанс: {r}') 
        
        
class Dragon(Hero):
    def __init__(self, name, health, armor, strong, mana, skin, fury) -> None:
        super().__init__(name, health, armor, strong)
        self.mana = mana
        self.fury = fury
        self.skin = skin

    def print_info(self, sep="-"):
        info =  f"{sep*50}\n" \
                f"{super()._get_info()}\n"  \
                f"{sep*20}\n" \
                f"Мана - {self.mana}\n"  \
                f"Броня - {self.skin}\n"  \
                f"Спец навык(ярость) - {self.fury}"
        print(info)      
    
    def special_attack(self, other):
        other.armor -= (self.strong + self.fury)
        if other.mana > 15 and other.armor < 0:
            other.health += other.armor
            other.armor = 0




class Arena:
    def __init__(self, warriors: list) -> None:
        self.warriors = warriors
        if type(warriors) == list:
            print(warriors)
        else:
            warriors = []
            print("not a list.")
        return warriors
    
    lst = []
    
    @staticmethod
    def add_warrior(warr):
        if warr not in Arena.lst:
            Arena.lst.append(warr)
        else:
            ValueError("Воин уже на арене")
        
    def choose_warrior():
        warrior_random = random.choice(Arena.lst)
        print(warrior_random)
        return warrior_random    

    def battle():
        if len(Arena.lst) > 2:
            return True
        else:
            ValueError("Количество воинов на арене должно быть больше 1")

    



fireball = Spell('Fireball')         
firebolt = Spell('Firebolt')        

hero1 = Hero('Dimitri', 50, 20, 15)    
hero2 = Hero('Alex', 60, 10, 5)    
hero3 = Mag('Gendalf', 30, 25, 10, 30, [fireball])   
hero4 = Archer("Elf", 40, 30, 5, 5, -5, [firebolt]) 
hero5 = Dragon("Fafnir", 70, 40, 30, 120, -20, 20)

# print(hero3.base_spell.name)
# hero1.print_info()
# hero4.print_info()
# hero5.print_info()

# print(hero4.mana)
hero3.print_info()
hero2.kick(hero3)
hero3.print_info()
hero2.kick(hero3)
# hero3.print_info()
# hero2.kick(hero3)

# hero5.print_info()
# hero4.kick(hero3)
# hero3.print_info()


print(Arena.lst)
Arena.add_warrior(hero1.name)
Arena.add_warrior(hero2.name)
Arena.add_warrior(hero3.name)
Arena.add_warrior(hero4.name)
Arena.add_warrior(hero5.name)
print(Arena.lst)