import logging
from functools import lru_cache
from typing import Optional, Union

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )
    # Site Settings
    APP_NAME: str = "sample"
    APP_SUMMARY: str = ""
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "fastapi sample"
    LOG_LEVEL: int = logging.INFO
    DEBUG: bool = False

    @field_validator("DEBUG", mode="before")
    @classmethod
    def parse_debug(cls, v: Union[str, bool], values: ValidationInfo):
        if isinstance(v, str):
            return v.upper() in ["T", "TRUE", "1"]
        return v


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )
    # Database Settings
    DB_SCHEME: Optional[str] = None
    DB_USERNAME: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[int] = None
    DB_PATH: Optional[str] = None
    DATABASE_DSN: Optional[PostgresDsn] = None

    @field_validator("DATABASE_DSN", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo):
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme=values.data.get("DB_SCHEME", "postgresql+asyncpg"),
            username=values.data.get("DB_USERNAME"),
            password=values.data.get("DB_PASSWORD"),
            host=values.data.get("DB_HOST"),
            port=int(values.data.get("DB_PORT")),
            path=values.data.get("DB_PATH"),
        )


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def get_db_settings():
    return DatabaseSettings()
