from pydantic import BaseModel, BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    residential_server_url: str = "http://10.32.13.57:8069"
    uvicorn_host: str = "10.32.47.62"
    uvicorn_port: int = 8000

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
    












