import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    residential_server_url: str = "http://157.245.62.74:8069"
    uvicorn_host: str = "157.245.62.74"
    uvicorn_port: str = "8081"

    db_host: str = "157.245.62.74"
    db_port: str = "5432"
    db_user: str = "adminapp"
    db_password: str = "adminapp2022"
    db_name: str = "odoo_db"
    db_echo: bool = False

    datetime_format = "%d/%m/%Y %H:%M:%S"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

DB_URL = f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}" \
         f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
