from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class RestaurantOwner(Base):
    __tablename__ = "restaurant_owners"

    ownerId = Column(Integer, ForeignKey('users.userId'), primary_key=True, index=True)
    user = relationship("User", back_populates="restaurant_owner")
    promotions = relationship("Promotion", back_populates="owner")