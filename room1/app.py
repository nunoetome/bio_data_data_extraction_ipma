
# app.py
import logging
#import mylib
import json
import configparser

logger = logging.getLogger(__name__)


# In-code configuration
#
# Config here the logging level
log_level = logging.INFO
# log_level = logging.DEBUG
# log_level = logging.WARNING
# log_level = logging.ERROR
# log_level = logging.CRITICAL

SETTINGS_FILE_PATH = 'settings.json'




def load_settings():
    with open(SETTINGS_FILE_PATH, 'r') as file:
        settings = json.load(file)
    return settings


def main():

    logger.info('Started')
    
    logger.info('Finished')

    load_settings()

    settings = load_settings()
    logger.info(f'Settings loaded: {settings}')
    
    
    
if __name__ == '__main__':
    logging.basicConfig(level=log_level)
    logger.info('Application is starting...')
    main()