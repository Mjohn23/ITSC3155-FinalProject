from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import payment as controller
from ..schemas import payment as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payment'],
    prefix="/payments"
)

@router.post("/", response_model=schema.Payment)
def create_payment(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Payment])
def read_payments(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=schema.Payment)
def read_one_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=payment_id)

@router.put("/{payment_id}", response_model=schema.Payment)
def update_one_payment(payment_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=payment_id)

@router.delete("/{payment_id}")
def delete_one_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=payment_id)