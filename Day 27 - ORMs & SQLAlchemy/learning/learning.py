# from sqlalchemy import create_engine, text

# engine = create_engine('sqlite:///mydb.db', echo=True)

# conn = engine.connect()
# conn.execute(text('CREATE TABLE IF NOT EXISTS people(name str, age int)'))

# conn.commit()

# from sqlalchemy.orm import Session
# session = Session(engine)
# session.execute(text('INSERT INTO people(name, age) VALUES("Mike", 30);'))
# session.commit()



from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,insert

engine = create_engine('sqlite:///mydb.db', echo=True)
meta = MetaData()
people = Table(
    'people',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable = False),
    Column('age', Integer)
)

meta.create_all(engine)

conn = engine.connect()



#! insert data 1
# #?without insert from sqlarchemy
# insert_stmt = people.insert().values(name='mike',age = 20)

#! insert data 2
# #?with insert from sqlarchemy
# insert_stmt = insert(people).values(name='jane',age = 40)
# result = conn.execute(insert_stmt)
# conn.commit()



#! select data From Databse  
select_stmt = people.select()
# .where(people.c.age > 20)
result = conn.execute(select_stmt)

for row in result.fetchall():
    print(row)


# print(1)