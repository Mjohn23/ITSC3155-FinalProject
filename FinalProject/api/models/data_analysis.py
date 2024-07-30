from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class DataAnalysis(Base):
    __tablename__ = "data_analysis"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    data = Column(String(100))
    analysis_date = Column(DateTime, default=lambda: datetime.now())
