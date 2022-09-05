from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name = "FastAPI Sample"
    app_version = "1.0.0"
    debug = False
    database_url = "sqlite:///./db.sqlite3"

    class Config:
        env_file = ".env"
