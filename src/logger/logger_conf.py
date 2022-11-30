import logging
import os
from typing import Final

LOGGER_PATH: Final = 'src/logger/logging_errors/error.log'

logger = logging.getLogger('error_logger')

if not os.path.exists(LOGGER_PATH):
    os.mkdir('src/logger/logging_errors')

with open(LOGGER_PATH, 'w'):
    print('initialized logger file!!!')

file_handler = logging.FileHandler(LOGGER_PATH)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_logger():
    return logger
