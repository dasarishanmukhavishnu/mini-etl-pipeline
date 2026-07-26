import csv
import logging

from models.order import Order
from exceptions import custom_exceptions


class CSVWriter:
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger

    def write(self,orders: list[Order],filepath: str) -> None:

        self.logger.info(f"Writing {len(orders)} records to {filepath}")
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "order_id",
                    "customer_name",
                    "city",
                    "age",
                    "signup_date",
                    "order_amount",
                    "payment_method",
                    "notes"
                ])

                for order in orders:
                    writer.writerow([
                        order.order_id,
                        order.customer_name,
                        order.city,
                        order.age,
                        order.signup_date,
                        order.order_amount,
                        order.payment_method,
                        order.notes
                    ])

            self.logger.info(f"Successfully wrote {len(orders)} records.")

        except Exception as e:
            self.logger.exception("Failed while writing CSV.")
            raise FileWriteError(str(e))