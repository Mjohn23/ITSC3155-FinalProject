from . import orders, customer, data_analysis, feedback, order_menu_item

def load_routes(app):
    app.include_router(orders.router)
    app.include_router(customer.router)
    app.include_router(data_analysis.router)
    app.include_router(feedback.router)
    app.include_router(order_menu_item.router)
