# user
# posts
import os
from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    String,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conn = 'sqlite:///' + os.path.join(BASE_DIR, 'blog.db')

engine = create_engine(conn)

Base = declarative_base()

"""
class User:
    id:int pk
    username:str
    email:str
class Post:
    id:int pk
    title:str
    content:str
    user_id:int foreignkey
    
"""


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=True)
    posts = relationship('Post', back_populates='author', cascade='all, delete')


    def __repr__(self):
        return f"<User {self.username} email{self.email}>"


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer(), primary_key=True)
    title = Column(String(45), nullable=False)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')

    # back_populates is use on both table while backref is use on one table

    def __repr__(self):
        return f"<User {self.title}, content{self.content}>"


# creates the database

Base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)
