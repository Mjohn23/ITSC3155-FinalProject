from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    ingredients: str
    price: float
    category: str
    calories: int

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    calories: Optional[int] = None

class MenuItem(MenuItemBase):
    menu_item_id: int

    class ConfigDict:
        from_attributes = True
