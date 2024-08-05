from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import customer as controller
from ..schemas import customer as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Customer'],
    prefix="/customers"
)

@router.post("/", response_model=schema.Customer)
def create_customer(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Customer])
def read_customers(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{customer_id}", response_model=schema.Customer)
def read_one_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=customer_id)

@router.put("/{customer_id}", response_model=schema.Customer)
def update_one_customer(customer_id: int, request: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=customer_id)

@router.delete("/{customer_id}")
def delete_one_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=customer_id)
