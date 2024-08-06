from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class Ingredient(BaseModel):
    name: str
    quantity: int
    quantity_required: int

class MenuItemBase(BaseModel):
    name: str
    ingredients: List[Dict[str, Any]]  # List of dictionaries
    price: float
    category: str
    calories: int

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    ingredients: Optional[List[Dict[str, Any]]] = None  
    price: Optional[float] = None
    category: Optional[str] = None
    calories: Optional[int] = None

class MenuItem(MenuItemBase):
    menu_item_id: int

    class Config:
        orm_mode = True
