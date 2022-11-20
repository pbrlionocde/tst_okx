import logging

logger = logging.getLogger('error_logger')

file_handler = logging.FileHandler('logger/logging_errors/error.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_logger():
    return logger
