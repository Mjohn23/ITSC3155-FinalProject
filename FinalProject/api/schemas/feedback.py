from pydantic import BaseModel
from typing import Optional
from .customer import Customer
from .orders import Order

class FeedbackBase(BaseModel):
    rating: int
    comments: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    customer_id: int
    order_id: int

class FeedbackUpdate(BaseModel):
    rating: Optional[int] = None
    comments: Optional[str] = None

class Feedback(FeedbackBase):
    feedback_id: int
    customer: Customer
    order: Order

    class Config:
        from_attributes = True
