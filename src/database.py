import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_URL

logger = logging.getLogger(__name__)

engine = create_engine(DB_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=True)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.exception('Session rollback cause EX: ' + str(e.args[0]))
        db.rollback()
        raise
    finally:
        db.close()



