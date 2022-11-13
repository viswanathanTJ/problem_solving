import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt= '%d-%m-%Y %I:%M:%S'
)

logger = logging.getLogger('logpy')
logger.warning("my warning")
logger.info('my info')
logger.critical('critical')
logger.error('error')
def debug():
    logger.debug('debug')
debug()