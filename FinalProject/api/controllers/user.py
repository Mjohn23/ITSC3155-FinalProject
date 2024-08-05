from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import user as model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas.user import UserCreate, UserUpdate

def create(db: Session, request: UserCreate):
    new_user = model.User(
        name=request.name,
        email=request.email,
        phone=request.phone,
        password=request.password,
        role=request.role
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_user

def read_all(db: Session):
    try:
        result = db.query(model.User).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, user_id: int):
    try:
        user = db.query(model.User).filter(model.User.userId == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return user

def update(db: Session, user_id: int, request: UserUpdate):
    try:
        user = db.query(model.User).filter(model.User.userId == user_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
        update_data = request.dict(exclude_unset=True)
        user.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return user.first()

def delete(db: Session, user_id: int):
    try:
        user = db.query(model.User).filter(model.User.userId == user_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
        user.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)