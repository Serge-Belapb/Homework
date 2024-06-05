import sqlalchemy as db

engine = db.create_engine('sqlite:///users_sqlalchemy.db')

connection = engine.connect()  # подсоединяемся к нашей БД

metadata = db.MetaData()   # инфа о таблицах, которые будут использоваться в нашей БД   

users = db.Table('Users', metadata,
            db.Column('user_id', db.Integer, primary_key=True),
            db.Column('user_name', db.Text), 
            db.Column('user_login', db.Text), 
            db.Column('user_password', db.Text), 
            db.Column('user_is_blocked', db.Boolean), 
            db.Column('subscription_date', db.Text), 
            db.Column('subscription_mode', db.Text), 
                
)