from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class DataAnalysisBase(BaseModel):
    data: str
    analysis_date: Optional[datetime] = True

class DataAnalysisCreate(DataAnalysisBase):
    analysis_id: int

class DataAnalysisUpdate(BaseModel):
    data: Optional[str] = None

class DataAnalysis(DataAnalysisBase):
    analysis_id: int
    data: str
    analysis_date: datetime

class ConfigDict:
    from_attributes = True