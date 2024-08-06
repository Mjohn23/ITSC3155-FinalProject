from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu_item as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['MenuItem'],
    prefix="/menu_items"
)

@router.post("/", response_model=schema.MenuItem)
def create_menu_item(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.MenuItem])
def read_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{menu_item_id}", response_model=schema.MenuItem)
def read_one_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=menu_item_id)

@router.put("/{menu_item_id}", response_model=schema.MenuItem)
def update_menu_item(menu_item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=menu_item_id)

@router.delete("/{menu_item_id}")
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=menu_item_id)
