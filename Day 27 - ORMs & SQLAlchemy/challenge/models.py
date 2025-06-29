
#? Table model

from sqlalchemy import Column, Integer, String
from database import Base  #? From databse.py file

class BookInfo(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key= True, index=True)
    title = Column(String)
    author = Column(String)
  