from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    phone: str
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str
    phone: str
    role: str

class User(UserBase):
    userId: int

class ConfigDict:
    from_attributes = True