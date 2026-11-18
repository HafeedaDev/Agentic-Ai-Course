from dataclasses import dataclass
from pydantic import BaseModel 


@dataclass
class A:
    age: int 

class B(BaseModel):
    age: int 

x = A("hello")
print(x)
try:
    y = B(age="hello")
except Exception as e:
    print("Pydantic blocked it:", e)