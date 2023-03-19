import mysql.connector
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(BASE_DIR, "site.db")

Base = declarative_base()

engine = create_engine(connection_string, echo=True)

Session = sessionmaker()


"""
class User
    Attributes:
    __tablename__ (str): The table name of the class
    id int
    username str
    email str
    date_created
"""


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


user1 = User(id=1, username='Attempt', email='akoatem@gmail.com')
print(user1)
