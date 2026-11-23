

# from pydantic import BaseModel, field_validator

# class Person(BaseModel):
#      age: int

#      @field_validator("age", mode="before")
#      @classmethod
#      def guard_before(cls, value):
#           print("Before Guard:" ,repr(value), type(value))
#           return value
     
#      @field_validator("age", mode="after")
#      @classmethod
#      def guard_after(cls, value):
#           print("After Gurd: ", repr(value), type(value))
#           return value

# Person(age="25")

# Person(age=35)



from pydantic import BaseModel, field_validator,ValidationError

class Meeting(BaseModel):
     title: str

     @field_validator("title", mode="after")
     @classmethod
     def remove_space(cls,value):
          cleaned = value.strip()
          if not cleaned:
               raise ValueError("Title not be none")
          return cleaned

m = Meeting(title= "       Standup    ")

print(repr(m.title))

