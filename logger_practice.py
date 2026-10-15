import logging

# logging.basicConfig(
#     level = logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# )

# logger = logging.getLogger(__name__)
# logger.info("This is  a test message")

from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    "small_test.log",
    maxBytes=200,
    backupCount=3
)

logger.addHandler(handler)

for i in range(50):
    logger.info(f"This is log message number {i}")


