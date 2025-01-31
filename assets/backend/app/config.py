from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # DATABASE_URL: str = "sqlite:///reflex.db"

    # Postgres offline
    DATABASE_URL: str = (
        "postgresql+psycopg2://postgres:antony15@localhost:5432/little_sun"
    )
    # Postgres railway online
    # DATABASE_URL: str = "postgresql://postgres:FiCsmdJUleAFwRRCfeHXptiufyAJBvcJ@roundhouse.proxy.rlwy.net:19329/railway"
    PROJECT_NAME: str = "little_sun"


@lru_cache()
def get_settings():
    return Settings()
