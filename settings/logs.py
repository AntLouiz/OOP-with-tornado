import sys
import re
import logging
import os.path
from collections import namedtuple
from settings import BASE_DIR


class CardFormatterPattern:

    def __init__(self, regex=r'\d{16}'):
        self.regex = re.compile(regex)

    def repl(self, matched_groups):
        matched_string = matched_groups.group(0)
        initial = matched_string[:4]
        middle = '*' * 8
        final = matched_string[12:]

        return f"{initial}{middle}{final}"

class CustomFormatter:
    def __init__(self, original_formatter, patterns):
        self.original_formatter = original_formatter
        self._patterns = patterns

    def format(self, record):
        if not record:
            return record

        msg = self.original_formatter.format(record)
        for pattern in self._patterns:
            msg = re.sub(pattern.regex, pattern.repl, msg)
        return msg

    def __getattr__(self, attr):
        return getattr(self.original_formatter, attr)


card_pattern = CardFormatterPattern()
logging_patterns = [
    card_pattern
]

LOGS_DIR = os.path.join(BASE_DIR, 'logs')

filename = os.path.join(LOGS_DIR, 'app.log')
log_format = '%(asctime)s - %(levelname)s - %(message)s'
level = logging.DEBUG

logging.basicConfig(format=log_format, filename=filename, level=level, filemode='a')

logger = logging.getLogger()

stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)

for handler in logger.root.handlers:
    formatter = handler.formatter
    if not formatter:
        break

    custom_formatter = CustomFormatter(formatter, logging_patterns)
    handler.setFormatter(custom_formatter)
