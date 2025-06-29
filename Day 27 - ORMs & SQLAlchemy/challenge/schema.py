
#? Request & response models
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str 

class BookCreate(BaseModel):
    pass

class BookRes(BaseModel):
    id: int

    class Config:
        orm_mode = True
    #  This allows Pydantic to work with SQLAlchemy models.
    #  SQLAlchemy gives you real Python objects (not just plain dictionaries). 
    #  orm_mode = True helps Pydantic understand how to read from those objects.

