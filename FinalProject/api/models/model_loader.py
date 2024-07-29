from . import user, customer, orders, menu_item, promotion, data_analysis, feedback, payment
from ..dependencies.database import engine

def index():
    user.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    data_analysis.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)


