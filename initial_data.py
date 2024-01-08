import logging

from src.db.db import SessionLocal
from src.db.init_db import init_users

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    try:
        init_users(db)
        logger.info("Users data has been successfully injected")
    except Exception as e:
        logger.error("A error occured during data injection", e)

def main() -> None:
    logger.info("Creating initial data...")
    init()
    logger.info("Initial data successfully created")

if __name__ == '__main__':
    main()