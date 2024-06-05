import sqlalchemy as db

engine = db.create_engine('sqlite:///users_sqlalchemy.db')

connection = engine.connect()  # подсоединяемся к нашей БД

metadata = db.MetaData()   # инфа о таблицах, которые будут использоваться в нашей БД   

users = db.Table('users', metadata,
            db.Column('id', db.Integer, primary_key=True),
            db.Column('name', db.Text), 
            db.Column('login', db.Text), 
            db.Column('password', db.Text), 
            db.Column('is_blocked', db.Boolean), 
            db.Column('subscription_date', db.Text), 
            db.Column('subscription_mode', db.Text)
)

metadata.create_all(engine)   # создаем таблицу

insertion_query = users.insert().values([
    {"name":"Иванов", "login":"Ina_nov", "password":"Ghjw2", "is_blocked":False, 
        "subscription_date":"2024-5-20", "subscription_mode":"free"},
    {"name":"Петров", "login":"Pet_ov", "password":"5Fgbb", "is_blocked":False, 
        "subscription_date":"2024-4-20", "subscription_mode":"free"},
    {"name":"Сидоров", "login":"Sid_rov", "password":"nNb3i", "is_blocked":False, 
        "subscription_date":"2024-5-1", "subscription_mode":"free"}
])

# connection.execute(insertion_query)

select_all_query = db.select([users])    
select_all_result = connection.execute(select_all_query)   # выбираем все значения из таблицы users

print(select_all_result.fetchall())