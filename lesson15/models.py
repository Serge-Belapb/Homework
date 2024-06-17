from sqlalchemy import create_engine
from sqlalchemy import (Column, ForeignKey, Table, 
                        Integer, String, Text, Boolean, Date, DateTime)

from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.sql import func

sqlite_database = "sqlite:///users.db"

# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)

class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    login = Column(String(20))
    password = Column(String(25))
    is_blocked = Column(Boolean, default=False) 
    subscription_date = Column(DateTime, server_default=func.now())      
    updated_sub_date = Column(DateTime, server_default=func.now(), onupdate=func.now())
    subscription_mode = Column(String(10))


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    type_of = Column(Boolean, default=False)
    price = Column(Integer)
    period = Column(Date)


# создаем таблицы
Base.metadata.create_all(bind=engine)

print("База данных и таблица созданы")






