from dataclasses import dataclass
from pydantic import BaseModel 


@dataclass
class A:
    age: int 

class B(BaseModel):
    age: int 

x = A("hello")
print(x)

Y = B(age="hello")