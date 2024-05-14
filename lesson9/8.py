'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

spis = ["hello python", True, 123]

def str_z(sp):
    for i in sp:
        if 

f = filter(str.isalpha,spis)
print(list(f))
s1 = "".join(f)
print(s1)