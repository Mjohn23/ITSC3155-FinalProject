from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_menu_item as controller
from ..schemas import order_menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order Menu Item'],
    prefix="/order_menu_items"
)

@router.post("/", response_model=schema.OrderMenuItem)
def create_order_menu_item(request: schema.OrderMenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderMenuItem])
def read_order_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_menu_item_id}", response_model=schema.OrderMenuItem)
def read_one_order_menu_item(order_menu_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=order_menu_item_id)

@router.put("/{order_menu_item_id}", response_model=schema.OrderMenuItem)
def update_one_order_menu_item(order_menu_item_id: int, request: schema.OrderMenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=order_menu_item_id)

@router.delete("/{order_menu_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_order_menu_item(order_menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=order_menu_item_id)
