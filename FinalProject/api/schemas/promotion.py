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

class PromotionUpdate(BaseModel):
    discount_percentage: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class Promotion(PromotionBase):
    promotion_name: str
    discount_percentage: int
    start_date = datetime
    end_date = datetime

    class ConfigDict:
        from_attributes = True