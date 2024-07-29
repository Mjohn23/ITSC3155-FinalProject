from . import user, customer, orders, menu_item
from ..dependencies.database import engine

def index():
    user.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
