from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    total_amount = Column(DECIMAL, nullable=False)
    order_status = Column(String(255), nullable=False)  
    order_type = Column(String(255), nullable=False)  
    order_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    customer = relationship("Customer", back_populates="orders")
    order_menu_items = relationship("OrderMenuItem", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)
    feedbacks = relationship("Feedback", back_populates="order")
