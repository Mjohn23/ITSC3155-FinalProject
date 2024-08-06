from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import feedback as controller
from ..schemas import feedback as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Feedback'],
    prefix="/feedback"
)

@router.post("/", response_model=schema.Feedback)
def create_feedback(request: schema.FeedbackCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Feedback])
def read_feedback(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{feedback_id}", response_model=schema.Feedback)
def read_one_feedback(feedback_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=feedback_id)

@router.put("/{feedback_id}", response_model=schema.Feedback)
def update_one_feedback(feedback_id: int, request: schema.FeedbackUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=feedback_id)

@router.delete("/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_feedback(feedback_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=feedback_id)

@router.get("/low_reviews/{threshold}", response_model=list[schema.Feedback])
def read_low_reviews(threshold: int, db: Session = Depends(get_db)):
    return controller.read_low_reviews(db=db, threshold=threshold)
