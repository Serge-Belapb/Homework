<<<<<<< HEAD
from pyowm import OWM


owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()

gorod = input("Введите город: ")
observation = mgr.weather_at_place(gorod)

# from pprint import pprint
# print(dir(observation))
# d = observation.to_dict()
# pprint(d)

w = observation.weather
print(f"Температура в {gorod} ", w.temperature('celsius')['temp'])
print(f"Ощущается как ", w.temperature('celsius')['feels_like'])
print("Скорость ветра ", w.wind()['speed'])

import time
sr = w.sunrise_time()
ss = w.sunset_time()
sr = float(sr)
suns = time.gmtime(ss+2*60*60)
sunr = time.gmtime(sr+2*60*60)
print("Восход солнца в ", time.strftime("%H:%M %d %B %Y года ", sunr))
print("Закат солнца в ", time.strftime("%H:%M %d %B %Y года ", suns))



=======
from pyowm import OWM


owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()

gorod = input("Введите город: ")
observation = mgr.weather_at_place(gorod)

# from pprint import pprint
# print(dir(observation))
# d = observation.to_dict()
# pprint(d)

w = observation.weather
print(f"Температура в {gorod} ", w.temperature('celsius')['temp'])
print(f"Ощущается как ", w.temperature('celsius')['feels_like'])
print("Скорость ветра ", w.wind()['speed'])

import time
sr = w.sunrise_time()
ss = w.sunset_time()
sr = float(sr)
suns = time.gmtime(ss+2*60*60)
sunr = time.gmtime(sr+2*60*60)
print("Восход солнца в ", time.strftime("%H:%M %d %B %Y года ", sunr))
print("Закат солнца в ", time.strftime("%H:%M %d %B %Y года ", suns))



>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
