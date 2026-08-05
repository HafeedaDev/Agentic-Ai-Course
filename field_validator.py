from pydantic import BaseModel, field_validator, ValidationError

class UserRegistration(BaseModel):
    username: str
    email: str
    age: int

#     # 1. Clean username spaces
    @field_validator('username', mode='before')
    @classmethod
    def clean_username(cls, value: str) -> str:
        if isinstance(value, str):
            value = value.strip()
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        return value

#     # 2. Check age limits

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value: int) -> int:
        if value < 18 or value > 100:
            raise ValueError("Age must be between 18 and 100 for registration")
        return value

#     # 3. Convert email to lower case

    @field_validator('email', mode='before')
    @classmethod
    def normalize_email(cls, value: str) -> str:
        if isinstance(value, str):
            return value.lower().strip()
        return value


# # --- Testing the Model ---
try:
    user = UserRegistration(
        username="   John_doe   ",
        email="JOHN.DOE@EXAMPLE.COM",
        age='25'
    )
    print("Validation Successful!")
    print(f"Cleaned Username: {user.username}")
    print(f"Normalized Email: {user.email}")
    print(f"Age: {user.age}")

except ValidationError as e:
    print(f"Validation Error:\n{e}")


