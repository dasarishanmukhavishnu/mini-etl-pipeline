from datetime import datetime
from models.order import Order
from exceptions.custom_exceptions import ValidationError

class OrderValidator:
    Valid_payment_methods={'UPI','CARD','CASH','DEBIT'}
    def validator(self,order: Order) -> None:
        if not order.customer_name.strip():
            raise ValidationError(f"Customer name is missing. Order_id : {order.order_id}")
        
        if not order.age.strip():
            raise ValidationError(f"Age is missing. Order_id : {order.order_id}")
            
        try:
            age = int(order.age)
        except ValueError:
            raise ValidationError(f"Age must be numeric. Order_id : {order.order_id}")

        if 18 > age or age > 100:
            raise ValidationError(f"Age must be in between 0 to 100 invalid age:{order.age}. Order_id : {order.order_id}")
        
        if not order.order_amount.strip():
            raise ValidationError(f"Order_amount is missing. Order_id : {order.order_id}")
        
        try:
            order_amount= float(order.order_amount)
        except:
            raise ValidationError(f"Invalid order amount. Order_id : {order.order_id}")
        
        if order_amount <= 0:
            raise ValidationError(f"Ivalid amount must be greater than zero. Order_id : {order.order_id}")

        if not order.payment_method.upper() in self.Valid_payment_methods:
            raise ValidationError(f"Invalid payment method. Order_id : {order.order_id}")
        
        try:
            datetime.strptime(order.signup_date.strip(),'%Y-%m-%d')
        except ValueError:
            raise ValidationError(f"Invalid signup date. Order_id : {order.order_id}")