import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_prefix=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "env"),
    )


settings = Settings(DB_HOST="localhost", DB_PORT="5433", DB_NAME="postgres", DB_USER="Pavel", DB_PASSWORD="1111")


def get_db_url():
    return f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
