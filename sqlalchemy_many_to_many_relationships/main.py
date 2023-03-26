# many-to-many relationship

import os
from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    String,
    ForeignKey,
    Table
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = 'sqlite:///' + os.path.join(BASE_DIR, 'site.sqlite3')

engine = create_engine(connection_str)

Base = declarative_base()

"""
table association:
    product_id: Int foreign key(products_id)
    customer_id:int foreignkey(customer_id)
class Customer:
    id:int pk
    name:str
    
class Post:
    id:int pk
   name:str
    price:Int  
"""
# association_table bind the two table together
association_table = Table(
    'association',
    Base.metadata,
    Column('customer_id', ForeignKey('customers.id')),
    Column('product_id', ForeignKey('products.id'))
)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    name = Column(String(40), nullable=False)
    products = relationship('Product', secondary=association_table,
                            back_populates='customers')

    # String representation
    def __repr__(self):
        return f"<Customer {self.name}>"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer(), primary_key=True)
    name = Column(String(45), nullable=False)
    price = Column(Integer(), nullable=False)
    customers = relationship('Customer', secondary=association_table,
                             back_populates='products')

    # String representation

    def __repr__(self):
        return f"<Product{self.name}>"


# creates the database

Base.metadata.create_all(engine)
# bind sessionmaker to engine
session = sessionmaker()(bind=engine)
