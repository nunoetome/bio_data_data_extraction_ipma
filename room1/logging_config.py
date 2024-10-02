# - This file is part of the project "bio_data_data_extraction_ipma" 
# and was created by the project organization.


import logging
import inspect
import os


# ----------------- LOG CONFIGURATION -----------------
#
# Config here the logging level
# Just uncomment the desired level and comment the others

LOG_LEVEL_GLOBAL = logging.DEBUG
#LOG_LEVEL_GLOBAL = logging.INFO
#LOG_LEVEL_GLOBAL = logging.WARNING
#LOG_LEVEL_GLOBAL = logging.ERROR
#LOG_LEVEL_GLOBAL = logging.CRITICAL

LOG_LEVEL_FILE = logging.DEBUG
#LOG_LEVEL_FILE = logging.INFO
#LOG_LEVEL_FILE = logging.WARNING
#LOG_LEVEL_FILE = logging.ERROR
#LOG_LEVEL_FILE = logging.CRITICAL

LOG_LEVEL_CONSOLE = logging.DEBUG
#LOG_LEVEL_CONSOLE = logging.INFO
#LOG_LEVEL_CONSOLE = logging.WARNING
#LOG_LEVEL_CONSOLE = logging.ERROR
#LOG_LEVEL_CONSOLE = logging.CRITICAL

LOG_OUTPUT_FILE = 'app.log'

#LOG_FORMAT_FILE = '%(asctime)s - %(levelname)s - %(message)s - [%(filename)s - %(funcName)s]' 
LOG_FORMAT_FILE = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' 
LOG_FORMAT_CONSOLE = '%(levelname)s - %(message)s'
# ----------------- END OF LOG CONFIGURATION -----------------


LOGGER = logging.getLogger(__name__)

def ini_logging():
    
    # GLOBAL LOGGING CONFIGURATION
    LOGGER.setLevel(LOG_LEVEL_GLOBAL) 
    
    # FILE HANDLER LOGGING CONFIGURATION
    file_handler = logging.FileHandler(LOG_OUTPUT_FILE)
    file_handler.setLevel(LOG_LEVEL_FILE)
    file_handler_formatter = logging.Formatter(LOG_FORMAT_FILE)        
    file_handler.setFormatter(file_handler_formatter)
    LOGGER.addHandler(file_handler)
    
    
    LOGGER.debug('file: ini_logging started')
    LOGGER.debug('LOG_LEVEL_GLOBAL: $f', LOG_LEVEL_GLOBAL)
    LOGGER.debug('Application loading: log started to file')
    
    # CONSOLE HANDLER LOGGING CONFIGURATION
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler_formatter = logging.Formatter(LOG_FORMAT_CONSOLE)        
    console_handler.setFormatter(console_handler_formatter)
    LOGGER.addHandler(console_handler)
    LOGGER.debug('Application loading: log started to console')
    

    
    return LOGGER


