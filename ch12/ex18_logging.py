# p421

import logging

logging.basicConfig(level="DEBUG", filename="output/blue_ox.log")
logger = logging.getLogger("bunyan")
logger.debug("Where's my axe?")
# logger.warn("I need my axe")
logger.warning("I need my axe")
