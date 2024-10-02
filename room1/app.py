# app.py

# Description: Main application file

import logging
import json
import configparser

# In-code configuration
#
# Config here the logging level
# Just uncomment the desired level and comment the others
log_level = logging.DEBUG
#log_level = logging.INFO
#log_level = logging.WARNING
#log_level = logging.ERROR
#log_level = logging.CRITICAL

LOG_OUTPUT_FILE = 'app.log'

SETTINGS_FILE_PATH = 'settings.json'
#end of in-code configuration



LOGGER = logging.getLogger(__name__)

def ini_logging():
    logging.basicConfig(level=log_level)
   # logging.basicConfig(level=log_level)
   # LOGGER = logging.getLogger(__name__)
   # LOGGER.info('Logging configured')
    return LOGGER



def load_settings():
    with open(SETTINGS_FILE_PATH, 'r') as file:
        settings = json.load(file)
    return settings


def main():
    settings = load_settings()
    ini_logging()
    LOGGER.info('Application is starting...')
    LOGGER.debug(f'Settings loaded: {settings}')     

  
    
    
    LOGGER.info('Finished')
    
    
if __name__ == '__main__':
    main()