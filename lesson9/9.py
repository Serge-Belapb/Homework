'''
Дан словарь, 
ключ - название страны, значение - список городов, 
на вход поступает город, необходимо сказать из какой он страны
'''

slov = {"Belarus" : ["Minsk", "Grodno"], 
        "Russia" : ["Pskov", "Moscow"]

}

gorod = input("Ввыдите город: ")
for strany, goroda in slov.items():
    if gorod in goroda:
        print(f"Город {gorod} из страны {strany}")
        break
    else:
        print(f"Ошибка. Страна для {gorod} не найдена ")




        
