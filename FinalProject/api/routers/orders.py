from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import get_db
from datetime import date

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.post("/", response_model=schema.Order)
def create_order(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Order])
def read_all_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}", response_model=schema.Order)
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=order_id)

@router.put("/{order_id}", response_model=schema.Order)
def update_order(order_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=order_id)

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=order_id)

@router.get("/revenue/{order_date}", response_model=float)
def calculate_daily_revenue(order_date: date, db: Session = Depends(get_db)):
    return controller.calculate_daily_revenue(db=db, order_date=order_date)
