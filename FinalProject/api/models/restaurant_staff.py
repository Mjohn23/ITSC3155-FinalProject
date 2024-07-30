from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class RestaurantStaff(Base):
    __tablename__ = "restaurant_staff"

    staffId = Column(Integer, ForeignKey('users.userId'), primary_key=True, index=True)
    user = relationship("User", back_populates="restaurant_staff")