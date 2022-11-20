import logging
import os

logger = logging.getLogger('error_logger')

if not os.path.exists('logger/logging_errors/error.log'):
    with open('logger/logging_errors/error.log', 'w'):
        print('initialized logger file!!!')

file_handler = logging.FileHandler('logger/logging_errors/error.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_logger():
    return logger
