from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    password = Column(String(128), nullable=False)
    role = Column(String(50), nullable=False)

    customer = relationship("Customer", back_populates="user", uselist=False)
    restaurant_staff = relationship("RestaurantStaff", back_populates="user", uselist=False)
    restaurant_owner = relationship("RestaurantOwner", back_populates="user", uselist=False)