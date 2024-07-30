from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    promotion_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_name = Column(String(100), nullable=False)
    promo_code = Column(String(100), nullable=False)
    start_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    end_date = Column(DateTime, nullable=False)
    owner_id = Column(Integer, ForeignKey('restaurant_owners.ownerId'), nullable=False)

    owner = relationship("RestaurantOwner", back_populates="promotions")
