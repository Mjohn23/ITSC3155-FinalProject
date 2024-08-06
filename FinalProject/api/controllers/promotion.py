from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import promotion as model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas.promotion import ApplyPromoCode
from ..schemas.orders import Order

def create(db: Session, request):
    new_promotion = model.Promotion(
        promotion_name=request.promotion_name,
        promo_code=request.promoCode,
        discount_percentage=request.discount_percentage,
        start_date=request.start_date,
        end_date=request.end_date,
        ownerId=request.ownerId
    )

    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_promotion

def read_all(db: Session):
    try:
        result = db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id):
    try:
        promotion = db.query(model.Promotion).filter(model.Promotion.promotion_id == item_id).first()
        if not promotion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return promotion

def update(db: Session, item_id, request):
    try:
        promotion = db.query(model.Promotion).filter(model.Promotion.promotion_id == item_id)
        if not promotion.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
        update_data = request.dict(exclude_unset=True)
        promotion.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return promotion.first()

def delete(db: Session, item_id):
    try:
        promotion = db.query(model.Promotion).filter(model.Promotion.promotion_id == item_id)
        if not promotion.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
        promotion.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def apply_promo_code(db: Session, request: ApplyPromoCode):
    promotion = db.query(model.Promotion).filter(model.Promotion.promo_code == request.promo_code).first()
    if not promotion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
    
    order = db.query(Order).filter(Order.order_id == request.order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")

    order.total_amount -= order.total_amount * (promotion.discount_percentage / 100)

    try:
        db.commit()
        db.refresh(order)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return order
