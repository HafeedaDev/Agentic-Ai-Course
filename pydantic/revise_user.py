from pydantic import BaseModel, Field, ValidationError

class Product(BaseModel):
    name:str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

items = [
    {"name": "Pen", "price": 10, "stock": 50},
    {"name": "Book", "price": -20, "stock": 5},
    {"name": "Bag", "price": 500, "stock": "many"},
]

valid=[]
invalid_count = 0
for item in items:
    try:
        product = Product(**item)
        valid.append(product)
    except ValidationError:
        print(f"Invalid Item {item}")
        invalid_count +=1
print(f"{invalid_count} invalid, {len(valid)} valid")        







    
        




























# class User(BaseModel):
#     name: str
#     age: int = Field(ge = 0, le=120)

# try:
#     User(name="Hafi", age="abc")
# except ValidationError as e:
#     print(e)