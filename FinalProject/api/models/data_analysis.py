from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class DataAnalysis(Base):
    __tablename__ = "data analysis"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    data = Column(String(100))
    analysis_date = Column(datetime)