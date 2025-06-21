
#! 🎯 Challenge
#? -  Build a Pydantic model for a user profile with fields for 
#? name, email, and age, including validation for email format and age range (18–100)

from pydantic import BaseModel, EmailStr, field_validator

class user_profile(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('age')
    def valid_age(cls, age):
        if 18 <= age <= 100:
            return age
        raise ValueError(f'Age must be between 18 and 100. You entered: {age}')        
    
user_info = {
    'name' : 'Bushra', 
    'email' : 'Bushra@gmail.com', 
    'age' : 230
}    

print('_________________ validation for age range ________________________\n')

try:
    validUser = user_profile(**user_info)    
    print(validUser)
except ValueError as e:
    print(f'Value Error please check value {e}', e)    
 

print('\n____________________________*****_____________________________') 