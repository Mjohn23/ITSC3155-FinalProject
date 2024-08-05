from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import promotion as controller
from ..schemas import promotion as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotion'],
    prefix="/promotions"
)

@router.post("/", response_model=schema.Promotion)
def create_promotion(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Promotion])
def read_promotions(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promotion_id}", response_model=schema.Promotion)
def read_one_promotion(promotion_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=promotion_id)

@router.put("/{promotion_id}", response_model=schema.Promotion)
def update_one_promotion(promotion_id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=promotion_id)

@router.delete("/{promotion_id}")
def delete_one_promotion(promotion_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=promotion_id)