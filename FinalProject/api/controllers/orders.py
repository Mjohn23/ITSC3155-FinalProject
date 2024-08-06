from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import orders as model, menu_item as menu_model
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
import json

def create(db: Session, request):
    for item in request.order_menu_items:
        menu_item = db.query(menu_model.MenuItem).filter(menu_model.MenuItem.menu_item_id == item.menu_item_id).first()
        if menu_item:
            ingredients = json.loads(menu_item.ingredients)
            for ingredient in ingredients:
                available_quantity = ingredient['quantity']  
                required_quantity = ingredient['quantity_required'] * item.quantity
                if available_quantity < required_quantity:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Not enough {ingredient['name']} to fulfill the order."
                    )

    new_order = model.Order(
        customer_id=request.customer_id,
        total_amount=request.total_amount,
        order_status=request.order_status,
        order_type=request.order_type,
        order_date=request.order_date
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_order

def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.Order).filter(model.Order.order_id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update(db: Session, item_id: int, request):
    try:
        item = db.query(model.Order).filter(model.Order.order_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete(db: Session, item_id: int):
    try:
        item = db.query(model.Order).filter(model.Order.order_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def calculate_daily_revenue(db: Session, order_date: date):
    try:
        total_revenue = db.query(model.Order).filter(
            model.Order.order_date.cast(date) == order_date
        ).with_entities(
            model.Order.total_amount
        ).all()
        total_revenue = sum([order.total_amount for order in total_revenue])
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return total_revenue
