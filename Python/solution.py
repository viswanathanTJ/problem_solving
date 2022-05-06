from cmath import log
import logging

logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s\
    %(message)s', level=logging.info)

logging.warning('warning1')
logging.info('info1')
logging.critical('critical1')
logging.debug('debug1')
logging.error('error1')