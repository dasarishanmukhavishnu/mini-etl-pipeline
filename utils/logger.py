import logging 
import sys

def set_logger(name: str,log_file: str,level: str='INFO') -> logging.Logger:

    log_level= getattr(logging,level.upper(),logging.INFO)

    console_format= logging.Formatter("--=== %(message)s ===---")
    console_handler= logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_format)

    file_format= logging.Formatter(
        '[%(asctime)s] - %(levelname)s - [%(name)s.%(funcName)s: %(lineno)s] - %(message)s',
        datefmt= '%Y-%m-%d %H:%M:%S'
    )
    file_handler= logging.FileHandler(log_file,encoding='utf-8')
    file_handler.setFormatter(file_format)

    logger= logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate= False

    if logger.hasHandlers():
        logger.handlers.clear()
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
