import logging

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT, filename='logger/logging_errors/error.log')

logger = logging.getLogger('error_logger')
file_handler = logging.FileHandler('logger/logging_errors/error.log')
logger.addHandler(file_handler)

def get_logger():
    return logger
