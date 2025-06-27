from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# import os

# if os.path.exists("pdb1.db"):
#     os.remove("pdb1.db")

dbcreate = create_engine('sqlite:///pdb1.db', echo=True)

Session = sessionmaker(bind = dbcreate)
session = Session()
base = declarative_base() 

class Book(base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author = Column(String(50))

class autorInfo(base):
    __tablename__ ='author'
    name = Column(String(20))
    book_id = Column(Integer, primary_key=True)

base.metadata.create_all(dbcreate)

b1 = Book(id=101, title="Test Book", author="Author 1"),
b2 =    Book(id=102, title="Book Two", author="Author 2"),
b3 =    Book(id=103, title="Book Three", author="Author 3"),
b4 =    Book(id=4, title="Book Four", author="Author 4"),
b5 =    Book(id=5, title="Book Five", author="Author 5"),
b6 =    Book(id=6, title="Book Six", author="Author 6"),


session.add_all([b1,b2,b3])
session.commit()