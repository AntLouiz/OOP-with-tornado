import sys
import os.path
import logging

BASE_DIR = os.path.dirname(__file__)
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

filename = os.path.join(LOGS_DIR, 'app.log')
log_format = '%(asctime)s - %(levelname)s - %(message)s'
level = logging.DEBUG

logging.basicConfig(format=log_format, filename=filename, level=level)

logger = logging.getLogger('app')


stderr_handler = logging.StreamHandler(sys.stderr)
logger.addHandler(stderr_handler)
