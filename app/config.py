from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Users"
    admin_email: str
    repo: str
    dsn: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_config():
    return Settings()
