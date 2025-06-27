from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

import os


#? It prepares the connection to a database. If students.db doesn't exist yet, it will be created later only when you run Base.metadata.create_all(engine).
engine = create_engine('sqlite:///orm.db', echo=True) 

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base() #? For creatin table 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

    posts= relationship("Post", back_populates='user') 

class Post(Base):    
    __tablename__ = 'posts'
    id = Column(Integer, primary_key= True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='posts')




Base.metadata.create_all(engine)

user1 = User(name= 'Alice', email='alice@example.com')
user2 = User(name= 'Bob', email='bob@example.com')
post1 = Post(title='ALice First Post', content = "This is Alice First Post", user = user1 )
post2 = Post(title='ALice second Post', content = "This is Alice second Post", user = user1 )
post3 = Post(title='bobs First Post', content = "This is bobs First Post", user = user2 )


session.add_all([user1,user2,post1,post2,post3])
session.commit()

posts_with_users = session.query(Post, User).join(User).all()

for post,user in posts_with_users:
    print(f'{post.title} {user.name}')

Alice = session.query(User).filter_by(name ='Alice' ).first()
print('Alice') 
for post  in Alice.posts:
    print(f'{post.title}')

filters_post = session.query(Post).join(User).filter(User.name == 'Alice').all()
for post in filters_post:
    print(f'Title : {post.title}, Author: {post.user.name}')
# # session.add_all([user1,user2])
# # session.commit()

# users = session.query(User).filter_by(name ='Alice' ).first()
# print(users.name) 

# session.delete(users)
# session.commit()

# for user in users:
#     print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

 
# print(os.path.abspath("orm.db"))