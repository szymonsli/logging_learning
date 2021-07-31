import logging
import os

log_number = 0
if not os.path.exists("logs"):
    os.mkdir("logs")
while os.path.exists(f"logs/logger_{log_number}.log"):
    log_number += 1

FILE_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(module)s::%(funcName)s - %(message)s"
TIME_FORMAT = "%d-%m-%Y %H:%M:%S"
CONSOLE_LOG_FORMAT = "%(levelname)s - %(module)s::%(funcName)s  - %(message)s"
LOG_LEVEL = logging.DEBUG
LOG_FILE_PATH = f"logs/logger_{log_number}.log"
LOG_FILE_MODE = "w"
LOG_TO_FILE = True
LOG_TO_CONSOLE = True

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

if LOG_TO_FILE:
    fh = logging.FileHandler(LOG_FILE_PATH, mode=LOG_FILE_MODE)
    formatter_file = logging.Formatter(FILE_LOG_FORMAT, datefmt=TIME_FORMAT)
    fh.setFormatter(formatter_file)
    logger.addHandler(fh)

if LOG_TO_CONSOLE:
    ch = logging.StreamHandler()
    formatter_console = logging.Formatter(CONSOLE_LOG_FORMAT)
    ch.setFormatter(formatter_console)
    logger.addHandler(ch)
