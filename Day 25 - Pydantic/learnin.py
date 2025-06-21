
#? Defining models with pydantic, nested models, why it’s needed

from pydantic import BaseModel,EmailStr, field_validator

class User(BaseModel):
    name : str
    email : EmailStr
    acc_id : int

    #?Custom validation
    @field_validator('acc_id')
    def validate_Acc_id(cls, value):
        if value <= 0:
            raise ValueError(f'Acc must be +ve number : {value}')
        return value




# user1 = User( name ='Bushra', email = 'Bushra@gmail.com', acc_id = 2563)
# print(user1.acc_id)



#? validation -- EmailStr, field_validator

user2 = User( name ='Bushra', email = 'bushra@gmail.com', acc_id = 253)
print(user2)


userDataIntoJSON = user2.model_dump_json() # json() --> model_dump_json()
print(userDataIntoJSON)

user_dicOBj = user2.model_dump() # dict - model_dump
print(user_dicOBj)

json_str = '{"name":"Bushra","email":"bushra@gmail.com","acc_id":253}'

# user3 = User.model_dump_json(json_str) # parse_raw --> model_dump_json
# print(user3)

#? also we can do tis
# user_data = {
#     'name' : 'Bushra',
#     'email' : 'bushra@gmail.com',
#     'acc_id' : 2435
# }

# user = User(**user_data)
# print(user)




x:int = 5
print(x)