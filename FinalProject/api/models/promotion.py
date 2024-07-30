from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base



class Promotion(Base):
    __tablename__ = "promotions"

    promotionName = Column(String(100), primary_key = True, index = True, autoincrement = True)
    promoCode = Column(String, primary_key=True, index=True)
    start_date = Column(datetime)
    end_date = Column(datetime)
    owner_id = Column(Integer, ForeignKey('restaurant_owners.ownerId'), nullable=False)
    owner = relationship("RestaurantOwner", back_populates="promotions")
