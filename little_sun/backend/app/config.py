from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///reflex.db"
    PROJECT_NAME: str = "little_sun"


@lru_cache()
def get_settings():
    return Settings()
