from pydantic import BaseModel
from typing import Optional
from .user import User, UserCreate

class RestaurantOwnerBase(BaseModel):
    pass

class RestaurantOwnerCreate(RestaurantOwnerBase):
    user: UserCreate

class RestaurantOwnerUpdate(RestaurantOwnerBase):
    user: Optional[UserCreate] = None

class RestaurantOwner(RestaurantOwnerBase):
    ownerId: int
    user: User

    class ConfigDict:
        from_attributes = True
