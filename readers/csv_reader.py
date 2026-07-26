import csv
import logging
from readers.base_reader import BaseReader
from models.order import Order
from exceptions.custom_exceptions import FileReadError


class CSVReader(BaseReader):

    def __init__(self,file_path: str,logger: logging.Logger) -> None:
        self.file_path = file_path
        self.logger = logger
    
    def read(self) -> list[Order]:
        orders: list[Order] = []
        self.logger.info(f"Reading CSV file: {self.file_path}")

        try: 
            with open(self.file_path,'r',encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    order = Order(
                        order_id= row['order_id'],
                        customer_name=row['customer_name'],
                        city=row['city'],
                        age=  row['age'],
                        signup_date=row['signup_date'],
                        order_amount = row['order_amount'],
                        payment_method=row['payment_method'],
                        notes=row.get('notes')
                    )

                    orders.append(order)
                self.logger.info(f"Sucessfully loaded {len(orders)} records")
                return orders
        except FileNotFoundError:
            self.logger.info(f"File Not Found:{self.file_path}")
            raise FileReadError(f"File not found:{self.file_path}")
        except Exception as e:
            self.logger.info("Unexpected Error while reading the file")
            raise FileReadError(str(e))
