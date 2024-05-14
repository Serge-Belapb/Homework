"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

sl_temp = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

d = dict(sorted(sl_temp.items(), key=lambda x:x[1]))
print("По возрастанию:", d)
d = dict(sorted(sl_temp.items(), key=lambda x:x[1], reverse=True))
print("По убыванию", d)