from dataclasses import dataclass
from pydantic import BaseModel 


@dataclass
class A:
    age: int 

class B(BaseModel):
    age: int 

x = A("hello")  #type: ignore
print(x)
try:
    y = B(age="hello") #type: ignore
except Exception as e:
    print("Pydantic blocked it:", e)