<<<<<<< HEAD
from . import user, customer, orders, menu_item, promotion, data_analysis, order_menu_item
=======
from . import user, customer, orders, menu_item, promotion, data_analysis, feedback, payment
>>>>>>> fb8c1866438813300a5517d081a150c62fb4000c
from ..dependencies.database import engine

def index():
    user.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    data_analysis.Base.metadata.create_all(engine)
<<<<<<< HEAD
    order_menu_item.Base.metadata.create_all(engine)
=======
    feedback.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)


>>>>>>> fb8c1866438813300a5517d081a150c62fb4000c
