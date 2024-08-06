import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app  # Import your FastAPI app
from ..dependencies.database import Base, get_db
from ..models import MenuItem, OrderMenuItem, Order

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_create_order_insufficient_ingredients(db):
    menu_item = MenuItem(
        name="Pizza",
        ingredients=json.dumps([
            {"name": "Cheese", "quantity": 5, "quantity_required": 2},
            {"name": "Dough", "quantity": 3, "quantity_required": 1}
        ]),
        price=9.99,
        category="Main Course",
        calories=300
    )
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)

    response = client.post("/orders/", json={
        "customer_id": 1,
        "total_amount": 9.99,
        "order_status": "Pending",
        "order_type": "Delivery",
        "order_date": "2024-08-06T00:32:39.895Z",
        "order_menu_items": [
            {"menu_item_id": menu_item.menu_item_id, "quantity": 4}
        ]
    })

    assert response.status_code == 400
    assert response.json() == {"detail": "Not enough Cheese to fulfill the order."}

def test_create_order_sufficient_ingredients(db):
    menu_item = MenuItem(
        name="Pizza",
        ingredients=json.dumps([
            {"name": "Cheese", "quantity": 10, "quantity_required": 2},
            {"name": "Dough", "quantity": 10, "quantity_required": 1}
        ]),
        price=9.99,
        category="Main Course",
        calories=300
    )
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)

    response = client.post("/orders/", json={
        "customer_id": 1,
        "total_amount": 9.99,
        "order_status": "Pending",
        "order_type": "Delivery",
        "order_date": "2024-08-06T00:32:39.895Z",
        "order_menu_items": [
            {"menu_item_id": menu_item.menu_item_id, "quantity": 2}
        ]
    })

    assert response.status_code == 200
    assert response.json()["order_status"] == "Pending"
