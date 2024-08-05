from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .customer import Customer
from .payment import Payment

class OrderBase(BaseModel):
    total_amount: float
    order_status: str
    order_type: str
    order_date: Optional[datetime] = None

class OrderCreate(OrderBase):
    customer_id: Optional[int] = None

class OrderUpdate(BaseModel):
    total_amount: Optional[float] = None
    order_status: Optional[str] = None
    order_type: Optional[str] = None
    order_date: Optional[datetime] = None

class Order(OrderBase):
    order_id: int
    customer: Optional[Customer] = None
    payment: Optional[Payment] = None

    class ConfigDict:
        from_attributes = True
