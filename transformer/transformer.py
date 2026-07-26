from datetime import datetime

from models.order import Order


class OrderTransformer:
    """
    Cleans and standardizes a validated Order.
    """

    def transform(self, order: Order) -> Order:

        order.customer_name = order.customer_name.strip().title()
        order.city = order.city.strip().title()
        order.payment_method = order.payment_method.strip().upper()
        order.signup_date = datetime.strptime(
            order.signup_date,
            "%Y-%m-%d"
        ).strftime("%d-%m-%Y")
        order.order_amount = f"{float(order.order_amount):.2f}"
        order.age = str(int(order.age))
        if order.notes:
            order.notes = order.notes.strip().title()
        return order