
#? DB CREated and saved in 

from sqlalchemy import create_engine,Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import BookInfoFetch_fastapi

engine = create_engine('sqlite:///bookdb.db', connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = Session()
Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'
    __table_args__ = {'extend_existing': True}  
    id = Column(Integer, primary_key=True )
    title = Column(String) 
    author = Column(String)
    publishedDate = Column(Date)
    # description = Column(String)

Base.metadata.create_all(engine)

# --- HELPER: Safe date parsing ---
def parse_date(date_str):
    for fmt in ('%Y-%m-%d', '%Y-%m', '%Y'):
        try:
            return datetime.strptime(date_str, fmt).date()
        except Exception:
            continue
    return None

 
#Saving Book into db
books = BookInfoFetch_fastapi.books
All_books = []
for book in books:
    date = parse_date(book['publishedDate'])
    new_book = Books(id=book['bid'],title=book['title'],author = book['authors'], publishedDate = date)
    All_books.append(new_book)

for book in All_books:
    if not session.get(Books, book.id):
        session.add(book)

session.commit()



# print(f'DB Created and\nBook: {len(BookInfoFetch_fastapi.books)} Added\n\n')