import sys
import logging
import os.path
from settings import BASE_DIR

LOGS_DIR = os.path.join(BASE_DIR, 'logs')

filename = os.path.join(LOGS_DIR, 'app.log')
log_format = '%(asctime)s - %(levelname)s - %(message)s'
level = logging.DEBUG

logging.basicConfig(format=log_format, filename=filename, level=level, filemode='a')

logger = logging.getLogger()


stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
