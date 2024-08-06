from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import restaurant_staff as controller
from ..schemas import restaurant_staff as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['RestaurantStaff'],
    prefix="/restaurant_staff"
)

@router.post("/", response_model=schema.RestaurantStaff)
def create_restaurant_staff(request: schema.RestaurantStaffCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.RestaurantStaff])
def read_restaurant_staffs(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{staffId}", response_model=schema.RestaurantStaff)
def read_one_restaurant_staff(staffId: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=staffId)

@router.put("/{staffId}", response_model=schema.RestaurantStaff)
def update_one_restaurant_staff(staffId: int, request: schema.RestaurantStaffUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=staffId)

@router.delete("/{staffId}")
def delete_one_restaurant_staff(staffId: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=staffId)
