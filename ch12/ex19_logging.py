# p422

import logging

fmt = "%(asctime)s %(levelname)s %(lineno)s %(message)s"
logging.basicConfig(level="DEBUG", format=fmt)
logger = logging.getLogger("bunyan")
logger.error("Where's my other plaid shirt?")
