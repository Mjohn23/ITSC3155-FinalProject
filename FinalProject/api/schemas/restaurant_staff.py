from pydantic import BaseModel
from typing import Optional
from .user import User, UserCreate

class RestaurantStaffBase(BaseModel):
    pass

class RestaurantStaffCreate(RestaurantStaffBase):
    name: str
    email: str
    phone: str
    password: str
    role: str

class RestaurantStaffUpdate(RestaurantStaffBase):
    pass

class RestaurantStaff(RestaurantStaffBase):
    staffId: int
    user: UserCreate

    class Config:
        from_attributes = True
