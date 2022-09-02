from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name = 'FastAPI Sample'
    app_version = '1.0.0'
    debug = False

    class Config:
        env_file = ".env"
