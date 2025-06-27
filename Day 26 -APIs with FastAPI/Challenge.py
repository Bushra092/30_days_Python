
#? 🎯 Challenge
#?-  Develop a FastAPI application with endpoints to manage a library of books, including creating, reading, updating, and deleting books

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {'book_id': 1, 'book_name': "Atomic Habits"},
    {'book_id': 2, 'book_name': "Deep Work"},
    {'book_id': 3, 'book_name': "The Psychology of Money"}
]

class Book(BaseModel):                          #?# Pydantic model to accept input for POST and PUT
    book_name: str

@app.get('/getItem/{book_id}')                  #?# GET single item 
def get_item(book_id: int):
    for book in books:
        if book['book_id'] == book_id:
            return {'result': book}
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")

@app.get('/getItems')                           #?# GET all or nth items
def get_items(nthBook: int = None):
    if nthBook:
        return books[:nthBook]
    return books

@app.post("/items/")                             #?# POST: Add new book
def post_item(book: Book):
    new_book_id = max(b['book_id'] for b in books) + 1 if books else 1
    new_book = {'book_id': new_book_id, 'book_name': book.book_name}
    books.append(new_book)
    return new_book


@app.put("/items/{book_id}")                      #?# PUT: Update existing book
def update_book(book_id: int, book: Book):
    for b in books:
        if b['book_id'] == book_id:
            b['book_name'] = book.book_name
            return b
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")

@app.delete("/items/{book_id}")                       #?# DELETE: Delete a book
def delete_item(book_id: int):
    for index, book in enumerate(books):
        if book['book_id'] == book_id:
            deleted_book = books.pop(index)
            return {'deleted': deleted_book}
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
