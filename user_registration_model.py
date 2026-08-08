from pydantic import BaseModel, Field, model_validator

class UserRegistration(BaseModel):
    username: str
    email: str
    password:str
    confirm_password: str
    age: int = Field(default=18)

    @model_validator(mode='after')

    def validate_password_age(self)->'UserRegistration':
        if  self.password != self.confirm_password:
            raise ValueError("Password do not Match")
        if   self.age < 18:
            raise ValueError("User must be  at least 18 years old")
        return self

    # Test case 1: Valid User
try:   
    user1 = UserRegistration(
        username="Ajith",
        email="ajith@example.com",
        password="securepassword123",
        confirm_password="securepassword123",
        age= 22
    )
    print("Success:", user1.model_dump())
except Exception as e:
    print("❌ Error:", e)

      # Test case 2: Pasword not Matching
try :     
    user2 = UserRegistration(
        username="Rahul",
        email="rahul@example.com",
        password="mysecretpassword",
        confirm_password="differentpassword",
        age = 29  
      )
    print("Success:",user2.model_dump())
except Exception as e:
    print("❌ Error:", e)    
