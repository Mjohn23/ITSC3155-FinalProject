from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    rating = Column(Integer, nullable=False)
    comments = Column(String, nullable=True)

    customer = relationship("Customer", back_populates="feedback")
    order = relationship("Order", back_populates="feedback")
