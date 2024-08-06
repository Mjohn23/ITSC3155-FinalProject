from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu_item as model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas.menu_item import MenuItemCreate, MenuItemUpdate

def create(db: Session, request: MenuItemCreate):
    new_menu_item = model.MenuItem(
        name=request.name,
        ingredients=request.ingredients,
        price=request.price,
        category=request.category,
        calories=request.calories
    )

    try:
        db.add(new_menu_item)
        db.commit()
        db.refresh(new_menu_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_menu_item

def read_all(db: Session):
    try:
        result = db.query(model.MenuItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.menu_item_id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update(db: Session, item_id: int, request: MenuItemUpdate):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.menu_item_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete(db: Session, item_id: int):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.menu_item_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)