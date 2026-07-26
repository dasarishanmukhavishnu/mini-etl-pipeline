from readers.base_reader import BaseReader
from validators.validator import OrderValidator
from transformer.transformer import OrderTransformer
from writers.writer import CSVWriter
from exceptions.custom_exceptions import (
    FileReadError,
    ValidationError,
    FileWriteError
)

class ETLPipeline:
    def __init__(
        self,
        reader: BaseReader,
        validator: OrderValidator,
        transformer: OrderTransformer,
        writer: CSVWriter,
        logger,
        cleaned_path: str,
        invalid_path: str
    ) -> None:

        self.reader = reader
        self.validator = validator
        self.transformer = transformer
        self.writer = writer
        self.logger = logger
        self.cleaned_path = cleaned_path
        self.invalid_path = invalid_path

    def run(self) -> None:

        self.logger.info("ETL Pipeline Started")
        try:
            orders = self.reader.read()
            valid_orders = []
            invalid_orders = []

            for order in orders:
                try:
                    self.validator.validator(order)
                    clean_order = self.transformer.transform(order)
                    valid_orders.append(clean_order)
                except ValidationError as e:
                    self.logger.warning(str(e))
                    invalid_orders.append(order)

            self.writer.write(valid_orders,self.cleaned_path)

            self.writer.write(invalid_orders,self.invalid_path)

            self.logger.info(
                f"Pipeline completed successfully.\n"
                f"Valid Orders: {len(valid_orders)} | "
                f"Invalid Orders: {len(invalid_orders)}"
            )
        except FileReadError as e:
            self.logger.error(str(e))

        except FileWriteError as e:
            self.logger.error(str(e))

        except Exception as e:
            self.logger.exception(f"Unexpected Error: {e}")