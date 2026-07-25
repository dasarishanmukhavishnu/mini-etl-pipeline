from dataclasses import dataclass
from typing import Optional

@dataclass
class Order:
    order_id: str
    customer_name: str
    city: str
    age: str
    signup_date: str
    order_amount: str
    payment_method: str
    notes: Optional[str] = None