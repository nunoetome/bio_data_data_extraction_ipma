# app.py

# Description: Main application file

import logging
import json
import configparser

# In-code configuration
#
# Config here the logging level
# Just uncomment the desired level and comment the others
LOG_LEVEL_GLOBAL = logging.DEBUG
#LOG_LEVEL_GLOBAL = logging.INFO
#LOG_LEVEL_GLOBAL = logging.WARNING
#LOG_LEVEL_GLOBAL = logging.ERROR
#LOG_LEVEL_GLOBAL = logging.CRITICAL

#LOG_LEVEL_FILE = logging.DEBUG
LOG_LEVEL_FILE = logging.INFO
#LOG_LEVEL_FILE = logging.WARNING
#LOG_LEVEL_FILE = logging.ERROR
#LOG_LEVEL_FILE = logging.CRITICAL

#LOG_LEVEL_CONSOLE = logging.DEBUG
#LOG_LEVEL_CONSOLE = logging.INFO
#LOG_LEVEL_CONSOLE = logging.WARNING
LOG_LEVEL_CONSOLE = logging.ERROR
#LOG_LEVEL_CONSOLE = logging.CRITICAL

LOG_OUTPUT_FILE = 'app.log'

SETTINGS_FILE_PATH = 'settings.json'
#end of in-code configuration



LOGGER = logging.getLogger(__name__)

def ini_logging():
    
    # GLOBAL LOGGING CONFIGURATION
    LOGGER.setLevel(LOG_LEVEL_GLOBAL) 

    LOGGER.debug('Application loading: log started')
    
    # FILE HANDLER LOGGING CONFIGURATION
    file_handler = logging.FileHandler(LOG_OUTPUT_FILE)
    file_handler.setLevel(LOG_LEVEL_FILE)
    file_handler_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')        
    file_handler.setFormatter(file_handler_formatter)
    LOGGER.addHandler(file_handler)
    LOGGER.debug('Application loading: log started to file')
    
    # CONSOLE HANDLER LOGGING CONFIGURATION
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    #console_handler_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')        
    #console_handler.setFormatter(console_handler_formatter)
    LOGGER.addHandler(console_handler)
    LOGGER.debug('Application loading: log started to console')
    
    return LOGGER



def load_settings():
    with open(SETTINGS_FILE_PATH, 'r') as file:
        settings = json.load(file)
    return settings


def main():
    settings = load_settings()
    ini_logging()
    LOGGER.critical("------------------")
    LOGGER.info('Application is starting...')
    LOGGER.debug(f'Settings loaded: {settings}')     


    
    LOGGER.info('Finished')
    
    
if __name__ == '__main__':
    main()