from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "sample"
    app_version: str = "1.0.0"
    description: str = "fastapi sample"
    debug: bool = True
    database_dsn: PostgresDsn
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings(
    database_dsn="postgresql+asyncpg://postgres:postgres@db:5432/sample"
)
