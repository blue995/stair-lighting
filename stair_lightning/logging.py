import logging
import logging.config
from yaml import load, Loader


def setup_logging():
    with open('logging.yaml') as f:
        yaml_conf_as_dict = load(f, Loader=Loader)
        logging.config.dictConfig(yaml_conf_as_dict)

def logging_sample():
    # create logger
    logger = logging.getLogger('simpleExample')

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')