from utils import load_config
from utils import set_logger

from readers.csv_reader import CSVReader
from validators.validator import OrderValidator
from transformer.transformer import OrderTransformer
from writers.writer import CSVWriter
from pipeline.pipeline import ETLPipeline


def main() -> None:

    # Load Configuration
    config = load_config("config/config.yaml")

    # Pipeline Details
    pipeline_name = config["pipeline"]["name"]
    pipeline_version = config["pipeline"]["version"]

    # Paths
    raw_data = config["paths"]["raw_data"]
    cleaned_data = config["paths"]["clean_data"]
    invalid_data = config["paths"]["invalid_data"]
    log_file = config["paths"]["log_file"]

    # Logging
    log_level = config["logging"]["level"]

    logger = set_logger(
        name=pipeline_name,
        log_file=log_file,
        level=log_level
    )

    logger.info(
        f"Starting {pipeline_name} (Version {pipeline_version})"
    )

    # Dependency Injection
    reader = CSVReader(raw_data, logger)
    validator = OrderValidator()
    transformer = OrderTransformer()
    writer = CSVWriter(logger)

    pipeline = ETLPipeline(
        reader=reader,
        validator=validator,
        transformer=transformer,
        writer=writer,
        logger=logger,
        cleaned_path=cleaned_data,
        invalid_path=invalid_data
    )

    pipeline.run()


if __name__ == "__main__":
    main()