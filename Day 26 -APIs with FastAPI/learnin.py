from fastapi import FastAPI ,HTTPException
from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, Field


class Piority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class todoBase(BaseModel):
    todo_name : str = Field(... , min_length=3, max_length=512 , description='Name of todo')
    todo_description : str = Field(..., description='Description of todo')
    piority : Piority = Field(default= Piority.LOW , description='piority of the todo')



class TodoCreate(todoBase):
    pass

class Todo(todoBase):
    todo_id: int = Field(..., description='Unique Identifier of the todo')



class TodoUpdate(BaseModel):
    todo_name :Optional[str] = Field(None , min_length=3, max_length=512 , description='Name of todo')
    todo_description : Optional[str] = Field(None, description='Description of todo')
    piority : Optional[Piority] = Field(None , description='piority of the todo')


app = FastAPI()

allTodos=  [

    Todo(todo_id  = 1, todo_name  = 'Sports', todo_description = 'Go Practice football', piority= Piority.HIGH),
    Todo(todo_id =2, todo_name = 'Read', todo_description = 'Read 10 pages' , piority= Piority.MEDIUM),
    Todo(todo_id = 3,todo_name ='Shop', todo_description = 'Go shopping' , piority= Piority.LOW),
    Todo(todo_id = 4,todo_name ='Study', todo_description ='Study for exam' , piority= Piority.MEDIUM),
    Todo(todo_id = 5,todo_name = 'Meditate',todo_description = 'Meditate 20 inutes' , piority= Piority.LOW)
    
]

 
#? PAth parameter http://127.0.0.1:8000/todo/1
@app.get('/todo/{todo_id}', response_model= Todo) 
def get_todo(todo_id: int):
    for todo in allTodos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')           
        

#? Querry parameter http://127.0.0.1:8000/todos?first_n=5

@app.get('/todos', response_model=List[Todo])
def get_todos(first_n:int = None):
    if first_n:
        return allTodos[:first_n]
    else: return allTodos



@app.post('/todos', response_model=Todo)
def create_todo(todo : TodoCreate):
    new_Todo_id = max(todo.todo_id for todo in allTodos)+1

    newTodo = Todo(todo_id = new_Todo_id, 
                   todo_name= todo.todo_name,
                   todo_description= todo.todo_description,
                   piority = todo.piority)
    # newTodo = {
    #     'todo_id': new_Todo_id,
    #     'todo_name': todo['todo_name'],
    #     'todo_description': todo['todo_description']
    # }
 
    allTodos.append(newTodo)
    return newTodo


@app.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo:TodoUpdate):
    for todo in allTodos:
        if todo.todo_id == todo_id:
            todo.todo_name = updated_todo.todo_name           
            todo.todo_description = updated_todo.todo_description  
            todo.piority = updated_todo.piority  
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')           


@app.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id:int):
    for ind, todo in enumerate(allTodos):
        if todo.todo_id == todo_id:
            delete_todo = allTodos.pop(ind)
            return delete_todo
    raise HTTPException(status_code=404, detail='Todo not found')           

        







#? #inbuild data validation
#? #inbuild documation #? docs  and redoc
#? # run is fast
#? # development time is less, less bug
# @app.get("/hello/{name}")
# async def hello(name):
#     return f"HELLO to fast api server {name}"

# class Available_Cuisines(str, Enum):
#     indian = 'indian' 
#     american = 'american'
#     italian = 'italian'

# food_items = {
#     'indian' : ["Samosa", "Dosa"],
#     'american': [ "Hot Dog", "Apple Pie"],
#     'italian': ["Ravioli", "Pizza"]
# }

# @app.get("/get_Item/{cuisine}")
# async def get_item(cuisine: Available_Cuisines):

#     return (f"Welcom to fastAPi \nYour Item is",
#             food_items.get(cuisine))

# couponCode = {
#     1: '10%',
#     2: '20%',
#     3: '30%'
# }

# @app.get("/get_coupon/{code}")
# async def get_coupon(code: int):
#     return {'Discount Amount': couponCode.get(code)}
    
 