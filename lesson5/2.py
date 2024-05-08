<<<<<<< HEAD
user1 = {'FIO':'Ivanov', 'Dol':'Direktor', 'GodRozh':'1990', 'Navyki': 'First', 'Deti':2}
user2 = {'FIO':'Petrov', 'Dol':'GlavBuh', 'GodRozh':'1995', 'Navyki': 'Second', 'Deti':1}
user3 = {'FIO':'Sidorov', 'Dol':'Spec', 'GodRozh':'1993', 'Navyki': 'Third', 'Deti':0}
users = [user1, user2, user3]
print(users[1])
s1 = input('Enter name:')
if s1 in users[0]['FIO']:
     print("Должность -", user1.get("Dol"), "Год рождения -", user1.get("GodRozh"), "Навыки -", user1.get("Navyki"), "Детей -", user1.get('Deti'))
elif s1 in users[1]['FIO']:
     print("Должность -", user2.get("Dol"), "Год рождения -", user2.get("GodRozh"), "Навыки -", user2.get("Navyki"), "Детей -", user2.get('Deti'))
else:
=======
user1 = {'FIO':'Ivanov', 'Dol':'Direktor', 'GodRozh':'1990', 'Navyki': 'First', 'Deti':2}
user2 = {'FIO':'Petrov', 'Dol':'GlavBuh', 'GodRozh':'1995', 'Navyki': 'Second', 'Deti':1}
user3 = {'FIO':'Sidorov', 'Dol':'Spec', 'GodRozh':'1993', 'Navyki': 'Third', 'Deti':0}
users = [user1, user2, user3]
print(users[1])
s1 = input('Enter name:')
if s1 in users[0]['FIO']:
     print("Должность -", user1.get("Dol"), "Год рождения -", user1.get("GodRozh"), "Навыки -", user1.get("Navyki"), "Детей -", user1.get('Deti'))
elif s1 in users[1]['FIO']:
     print("Должность -", user2.get("Dol"), "Год рождения -", user2.get("GodRozh"), "Навыки -", user2.get("Navyki"), "Детей -", user2.get('Deti'))
else:
>>>>>>> d64038ef74ba144a6ff00af923ff1a20353ae745
     print("Должность -", user3.get("Dol"), "Год рождения -", user3.get("GodRozh"), "Навыки -", user3.get("Navyki"), "Детей -", user3.get('Deti'))