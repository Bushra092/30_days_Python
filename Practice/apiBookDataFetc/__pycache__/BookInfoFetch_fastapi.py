# from fastapi import FastAPI, HTTPException


import requests

# GET: Fetch data from API
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=SEARCH_TERM")
data = response.json()
books = []
bookid = 0
for item in data.get('items', []):
    bookid = bookid+1
    newItem = {
    'bid' : bookid,
    'title' : item['volumeInfo']['title'],
    'authors' : item['volumeInfo']['authors'][0],
    'publishedDate' : item['volumeInfo']['publishedDate']
    }

    books.append(newItem)

for book in books:
    print(book)
    

# # #? API
# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

# # @app.get('/books')
# # def books():
# #     return books
# # @app.get('/books')
# # def get_books():
# #     try:
# #         response = requests.get("https://www.googleapis.com/books/v1/volumes?q=SEARCH_TERM")
# #         response.raise_for_status()
# #         data = response.json()
# #         books = []
# #         bookid = 0
# #         for item in data.get('items', []):
# #             bookid += 1
# #             newItem = {
# #                 'bid': bookid,
# #                 'title': item['volumeInfo'].get('title', 'N/A'),
# #                 'authors': item['volumeInfo'].get('authors', ['N/A'])[0],
# #                 'publishedDate': item['volumeInfo'].get('publishedDate', 'N/A')
# #             }
# #             books.append(newItem)
# #         return books
# #     except requests.RequestException as e:
# #         raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/books")
def get_books():
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=Harry+Potter")
    data = response.json()
    books = []
    bookid = 0
    for item in data.get('items', []):
        bookid += 1
        newItem = {
            'bid': bookid,
            'title': item['volumeInfo'].get('title', 'N/A'),
            'authors': item['volumeInfo'].get('authors', ['Unknown'])[0],
            'publishedDate': item['volumeInfo'].get('publishedDate', 'Unknown')
        }
        books.append(newItem)
    return books

