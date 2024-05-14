'''
Дан словарь, 
ключ - название страны, значение - список городов, 
на вход поступает город, необходимо сказать из какой он страны
'''

slov = {"Belarus" : ["Minsk", "Grodno"], 
        "Russia" : ["Pskov", "Moscow"]

}

gorod = input("Ввыдите город: ")
print(type(gorod))

otvet = filter(lambda x : True if x == gorod else False, slov)
print(list(otvet))