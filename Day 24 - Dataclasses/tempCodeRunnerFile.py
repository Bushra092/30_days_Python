
#! 🎯 Challenge
#? -  Create a dataclass to represent a library book with fields for title, author, ISBN, and publication year, including a method to display book details

from dataclasses import dataclass, asdict

@dataclass
class library_book:
    title: str
    author: str
    ISBN: int
    publication_year: int
    

book1_Details = library_book("To Kill a Mockingbird", "Harper Lee",  9780061120084, 1960)  

print('_______________________________________________________\n\nWith using dataclasses\n')

# User-friendly display using f-string (no method needed)
print(f" Title: {book1_Details.title}\n Author: {book1_Details.author} \n ISBN: {book1_Details.ISBN}\n Year: {book1_Details.publication_year}")  

# print(book1_Details)  #? Output shows the class name and all fields in a structured format

# print(asdict(book1_Details))  #? Converting the dataclass to a dictionary using asdict() Output: {'title': ..., 'author': ..., ...}

print('_______________________________________________________\n\nWithout using dataclasses\n')
class witoutDataclass():
    def __init__(self, title,author, ISBN, PublicY):        
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_year = PublicY

WDC_book1_Details = witoutDataclass("To Kill a Mockingbird", "Harper Lee",  9780061120084, 1960) 

#! This will just show the object reference unless __str__ or __repr__ is defined
print(WDC_book1_Details)  # Output: <__main__.WithoutDataclass object at 0x...>

print('End of Execution\n__________________________*****_________________________\n')