import logging
from datetime import datetime

def setup_logger():
    logger = logging.getLogger("heartbeat_logger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("hb_test.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger