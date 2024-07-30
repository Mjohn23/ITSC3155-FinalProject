from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)  
    ingredients = Column(String(255), nullable=False)  
    price = Column(DECIMAL, nullable=False)
    category = Column(String(255), nullable=False)  
    calories = Column(Integer, nullable=False)

    order_menu_items = relationship("OrderMenuItem", back_populates="menu_item")
