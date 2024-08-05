from pydantic import BaseModel
from typing import Optional
from .user import User

class CustomerBase(BaseModel):
    name: str
    phone: str
    address: str

class CustomerCreate(CustomerBase):
    userId: Optional[int] = None

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    customer_id: int
    user: Optional[User] = None

    class ConfigDict:
        from_attributes = True
