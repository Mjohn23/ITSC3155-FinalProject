from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import restaurant_owner as controller
from ..schemas import restaurant_owner as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['RestaurantOwner'],
    prefix="/restaurant_owners"
)

@router.post("/", response_model=schema.RestaurantOwner)
def create_restaurant_owner(request: schema.RestaurantOwnerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.RestaurantOwner])
def read_restaurant_owners(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{ownerId}", response_model=schema.RestaurantOwner)
def read_one_restaurant_owner(ownerId: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=ownerId)

@router.put("/{ownerId}", response_model=schema.RestaurantOwner)
def update_one_restaurant_owner(ownerId: int, request: schema.RestaurantOwnerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=ownerId)

@router.delete("/{ownerId}")
def delete_one_restaurant_owner(ownerId: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=ownerId)