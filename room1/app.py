
# app.py
import logging
import mylib

logger = logging.getLogger(__name__)

def main():
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')
    
    
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()