from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('users.userId'), nullable=True)
    name = Column(String(200), nullable=False)  
    phone = Column(String(20), nullable=False)  
    address = Column(String(200), nullable=True)

    user = relationship("User", back_populates="customer")
    orders = relationship("Order", back_populates="customer")
    feedbacks = relationship("Feedback", back_populates="customer")
