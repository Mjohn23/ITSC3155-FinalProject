from pydantic import BaseModel
from .user import User

class CustomerBase(BaseModel):
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    address: str

class Customer(CustomerBase):
    customerId: int
    user: User

    class Config:
        orm_mode = True