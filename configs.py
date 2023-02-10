import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    residential_server_url: str = os.getenv('RESIDENTIAL_SERVER_URL')
    uvicorn_host: str = os.getenv('UVICORN_HOST')
    uvicorn_port: str = os.getenv('UVICORN_PORT')

    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT")
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_name: str = os.getenv("DB_NAME")
    db_echo: bool = False

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


_db = get_settings()

DB_URL = f"postgresql+psycopg2://{_db.db_user}:{_db.db_password}@{_db.db_host}:{_db.db_port}/{_db.db_name}"
