from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .orders import Order
from .menu_item import MenuItem

class OrderMenuItemBase(BaseModel):
    order_menu_item_id: int
    quantity: int

class OrderMenuItemCreate(OrderMenuItemBase):
    pass

class OrderMenuItemUpdate(BaseModel):
    quantity: Optional[int] = None

class OrderMenuItem(OrderMenuItemBase):
    order_menu_item_id: int
    quantity: int
    order_id: int
    menu_item_id: int

    class ConfigDict:
        from_attributes = True