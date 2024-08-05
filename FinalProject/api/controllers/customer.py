from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import customer as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_customer = model.Customer(
        userId=request.userId,
        address=request.address
    )

    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_customer

def read_all(db: Session):
    try:
        result = db.query(model.Customer).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id):
    try:
        customer = db.query(model.Customer).filter(model.Customer.customer_id == item_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return customer

def update(db: Session, item_id, request):
    try:
        customer = db.query(model.Customer).filter(model.Customer.customer_id == item_id)
        if not customer.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
        update_data = request.dict(exclude_unset=True)
        customer.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return customer.first()

def delete(db: Session, item_id):
    try:
        customer = db.query(model.Customer).filter(model.Customer.customer_id == item_id)
        if not customer.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
        customer.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
