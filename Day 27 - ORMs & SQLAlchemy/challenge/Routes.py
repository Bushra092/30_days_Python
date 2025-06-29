

#? API
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session as SQLSession
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

from database import session as db_session, Books  # session and Books model

app = FastAPI()

class BookSchema(BaseModel):  #?  Pydantic schema to return Book data 
    id: int
    title: str
    author: str
    publishedDate: date | None   

    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    id: int
    title: str
    author: str
    publishedDate: Optional[date] = None  

class BookUpdate(BaseModel):
    title: str
    author: str
    publishedDate: date | None


 
def get_db():
    db = db_session
    try:
        yield db
    finally:
        db.close()
 
@app.get("/books", response_model=List[BookSchema])                     #?read_books
def read_books(db: SQLSession = Depends(get_db)):
    books = db.query(Books).all()
    return books

 
@app.delete("/books/{book_id}", response_model=BookSchema)             #!deleteBook  
def deleteBook(book_id: int, db: SQLSession = Depends(get_db)):
    book = db.query(Books).filter(Books.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return book


@app.put("/books/{book_id}", response_model=BookSchema)                 #?update_book
def update_book(book_id: int, updated_book: BookUpdate, db: SQLSession = Depends(get_db)):
    book = db.query(Books).filter(Books.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = updated_book.title
    book.author = updated_book.author
    book.publishedDate = updated_book.publishedDate

    db.commit()
    db.refresh(book)
    return book


@app.post("/books", response_model=BookSchema)                          #?create_book
def create_book(book: BookCreate, db: SQLSession = Depends(get_db)):
    existing_book = db.query(Books).filter(Books.id == book.id).first()
    if existing_book:
        raise HTTPException(status_code=400, detail="Book with this ID already exists")

    new_book = Books(
        id=book.id,
        title=book.title,
        author=book.author,
        publishedDate=book.publishedDate
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
