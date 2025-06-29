

#? Fetch Book data form API

import requests
 
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=SEARCH_TERM")
data = response.json() 
books = []
bookid = 0
for item in data.get('items', []):
    # print(response.json())
    bookid = bookid+1
    newItem = {
    'bid' : bookid,
    'title' : item['volumeInfo']['title'],
    'authors' : item['volumeInfo']['authors'][0],
    'publishedDate' : item['volumeInfo']['publishedDate'],
    'description': item['volumeInfo'][ 'description']

    }

    books.append(newItem)