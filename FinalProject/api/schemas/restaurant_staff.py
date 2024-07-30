from pydantic import BaseModel
from .user import User

class RestaurantStaffBase(BaseModel):
    pass

class RestaurantStaffCreate(RestaurantStaffBase):
    pass

class RestaurantStaffUpdate(RestaurantStaffBase):
    pass

class RestaurantStaff(RestaurantStaffBase):
    staffId: int
    user: User

    class Config:
        orm_mode = True