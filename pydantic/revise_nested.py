from pydantic import BaseModel, Field, ValidationError

class Address(BaseModel):
    city: str
    pincode: str

class Customer(BaseModel):
    name: str
    address: Address
try:
    customer = Customer(name="Hafi", address={"city": "Tirur"})
    print(customer.address.city)
except ValidationError as e:
    print(e)
