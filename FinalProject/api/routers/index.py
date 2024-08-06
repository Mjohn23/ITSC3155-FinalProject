from . import orders, customer, data_analysis, feedback,menu_item, order_menu_item, payment, promotion, restaurant_owner, restaurant_staff, user

def load_routes(app):
    app.include_router(orders.router)
    app.include_router(customer.router)
    app.include_router(data_analysis.router)
    app.include_router(feedback.router)
    app.include_router(menu_item.router) 
    app.include_router(order_menu_item.router)
    app.include_router(payment.router)
    app.include_router(promotion.router)
    app.include_router(restaurant_owner.router)
    app.include_router(restaurant_staff.router)
    app.include_router(user.router)
