from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import data_analysis as controller
from ..schemas import data_analysis as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Data Analysis'],
    prefix="/data_analysis"
)

@router.post("/", response_model=schema.DataAnalysis)
def create_data_analysis(request: schema.DataAnalysisCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.DataAnalysis])
def read_data_analysis(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{data_analysis_id}", response_model=schema.DataAnalysis)
def read_one_data_analysis(data_analysis_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=data_analysis_id)

@router.put("/{data_analysis_id}", response_model=schema.DataAnalysis)
def update_one_data_analysis(data_analysis_id: int, request: schema.DataAnalysisUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=data_analysis_id)

@router.delete("/{data_analysis_id}")
def delete_one_data_analysis(data_analysis_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=data_analysis_id)
