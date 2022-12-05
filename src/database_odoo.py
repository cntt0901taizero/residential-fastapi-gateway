from psycopg2 import pool
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import logging

logger = logging.getLogger(__name__)

SQLALCHAMY_DATABASE_URL = 'postgresql+psycopg2://admin:abbankadmin@10.32.13.58:5432/odoo_db_dev'
engine = create_engine(SQLALCHAMY_DATABASE_URL, poolclass=NullPool)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
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



