from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    payment_method = Column(String(50), nullable=False)  
    amount = Column(DECIMAL, nullable=False)
    payment_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    order = relationship("Order", back_populates="payment")
