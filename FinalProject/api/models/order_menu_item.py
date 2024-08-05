from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..dependencies.database import Base

class OrderMenuItem(Base):
    __tablename__ = "order_menu_item"

    order_menu_item_id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    quantity = Column(Integer)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"))

    order = relationship("Order", back_populates = "order_menu_items")
    menu_item = relationship("MenuItem", back_populates = "order_menu_items")