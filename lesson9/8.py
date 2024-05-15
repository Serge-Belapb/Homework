'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

spis = ["hello python", True, 123, "123"]

f = filter(lambda x : type(x) is str, spis)
print(list(f))
f = filter(lambda x : type(x) is bool, spis)
print(list(f))
