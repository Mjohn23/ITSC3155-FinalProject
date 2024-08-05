from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import restaurant_staff as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_staff = model.RestaurantStaff(
        staffId=request.staffId
    )

    try:
        db.add(new_staff)
        db.commit()
        db.refresh(new_staff)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_staff

def read_all(db: Session):
    try:
        result = db.query(model.RestaurantStaff).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id):
    try:
        staff = db.query(model.RestaurantStaff).filter(model.RestaurantStaff.staffId == item_id).first()
        if not staff:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RestaurantStaff not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return staff

def update(db: Session, item_id, request):
    try:
        staff = db.query(model.RestaurantStaff).filter(model.RestaurantStaff.staffId == item_id)
        if not staff.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RestaurantStaff not found!")
        update_data = request.dict(exclude_unset=True)
        staff.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return staff.first()

def delete(db: Session, item_id):
    try:
        staff = db.query(model.RestaurantStaff).filter(model.RestaurantStaff.staffId == item_id)
        if not staff.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RestaurantStaff not found!")
        staff.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)