from utils import load_config,set_logger


def main():

    config= load_config('config/config.yaml')
    logger = set_logger(
        name= config['pipeline']['name'],
        log_file= config['paths']['log_file'],
        level= config['logging']['level']
    )

    logger.info("---Sprint 1: Initialization of Config and Logger---")
    logger.info(f"Loaded pipeline Layout from config file and version : {config['pipeline']['version']}")
    logger.info(f"Started tracking the raw data path : {config['paths']['raw_data']}")

if __name__ == "__main__":
    main()