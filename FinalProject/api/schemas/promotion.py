from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    promoCode: str
    discount_percentage: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class PromotionCreate(PromotionBase):
    promotion_name: str
    ownerId: int

class PromotionUpdate(BaseModel):
    discount_percentage: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class Promotion(PromotionBase):
    promotion_name: str
    discount_percentage: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    ownerId: int

    class Config:
        from_attributes = True

class ApplyPromoCode(BaseModel):
    order_id: int
    promo_code: str
