from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import restaurant_owner as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_owner = model.RestaurantOwner(
        ownerId=request.ownerId
    )

    try:
        db.add(new_owner)
        db.commit()
        db.refresh(new_owner)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_owner

def read_all(db: Session):
    try:
        result = db.query(model.RestaurantOwner).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id):
    try:
        owner = db.query(model.RestaurantOwner).filter(model.RestaurantOwner.ownerId == item_id).first()
        if not owner:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RestaurantOwner not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return owner

def update(db: Session, item_id, request):
    try:
        owner = db.query(model.RestaurantOwner).filter(model.RestaurantOwner.ownerId == item_id)
        if not owner.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RestaurantOwner not found!")
        update_data = request.dict(exclude_unset=True)
        owner.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return owner.first()

def delete(db: Session, item_id):
    try:
        owner = db.query(model.RestaurantOwner).filter(model.RestaurantOwner.ownerId == item_id)
        if not owner.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RestaurantOwner not found!")
        owner.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
