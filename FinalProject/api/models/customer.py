from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, ForeignKey('users.userId'), primary_key=True, index=True)
    address = Column(String(200))

    user = relationship("User", back_populates="customer")
    orders = relationship("Order", back_populates="customer")
    feedbacks = relationship("Feedback", back_populates="customer")