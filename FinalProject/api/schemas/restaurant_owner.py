from pydantic import BaseModel
from .user import User

class RestaurantOwnerBase(BaseModel):
    pass

class RestaurantOwnerCreate(RestaurantOwnerBase):
    pass

class RestaurantOwnerUpdate(RestaurantOwnerBase):
    pass

class RestaurantOwner(RestaurantOwnerBase):
    ownerId: int
    user: User

    class Config:
        orm_mode = True