from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentBase(BaseModel):
    payment_method: str
    amount: float
    payment_date: Optional[datetime] = None

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(BaseModel):
    payment_method: Optional[str] = None
    amount: Optional[float] = None
    payment_date: Optional[datetime] = None

class Payment(PaymentBase):
    payment_id: int
    order: 'Order'  

    class Config:
        orm_mode = True
        from_attributes = True
