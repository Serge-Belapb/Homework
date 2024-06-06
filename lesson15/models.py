from sqlalchemy import (Column, ForeignKey, Table, 
                        Integer, String, Text, Boolean, Date, DateTime)

from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    login = Column(String(20))
    password = Column(String(25))
    is_blocked = Column(String(7), Boolean) 
    subscription_date = Column(DateTime, server_default=func.now())      
    subscription_mode = Column(String(10))
    quizes = relationship('Quiz', backref='user')
    created_at = Column()
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


quiz_question = Table(
            'quiz_question'
)


class Question(Base):
    __tablename__ = 'question' 

    id = Column(Integer(), primary_key=True)
    question = Column(String(250), nullable=False)
    answer = Column(String(100), nullable=False)
    wrong1 = Column(String(100), nullable=False)
    wrong2 = Column(DateTime, server_default=func.now())
    wrong3 = Column(DateTime, server_default=func.now(), onupdate=func.now())   




