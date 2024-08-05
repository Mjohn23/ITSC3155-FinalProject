from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import user as controller
from ..schemas import user as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['User'],
    prefix="/users"
)

@router.post("/", response_model=schema.User)
def create_user(request: schema.UserCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.User])
def read_users(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{user_id}", response_model=schema.User)
def read_one_user(user_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, user_id=user_id)

@router.put("/{user_id}", response_model=schema.User)
def update_one_user(user_id: int, request: schema.UserUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, user_id=user_id)

@router.delete("/{user_id}")
def delete_one_user(user_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, user_id=user_id)