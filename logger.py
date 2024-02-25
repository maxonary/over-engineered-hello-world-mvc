import logging

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def enable_logging():
    logger.setLevel(logging.INFO)

def disable_logging():
    logger.setLevel(logging.CRITICAL)