from logging import Formatter, StreamHandler

from core.config import get_logger, get_settings
from fastapi import FastAPI
from routers import api_router

_settings = get_settings()


def lifespan(app: FastAPI):
    sampleapp_log_handler = StreamHandler()
    sampleapp_log_handler.setFormatter(
        Formatter(
            "[%(pathname)s:%(lineno)d][%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S %z",
        )
    )
    _logger = get_logger()
    _logger.setLevel(_settings.LOG_LEVEL)
    _logger.addHandler(sampleapp_log_handler)
    _logger.debug(f"docs_url -> {app.docs_url}")
    _logger.debug(f"redoc_url -> {app.redoc_url}")
    yield


app = FastAPI(
    title=_settings.APP_NAME,
    summary=_settings.APP_SUMMARY,
    version=_settings.APP_VERSION,
    description=_settings.APP_DESCRIPTION,
    debug=_settings.DEBUG,
    lifespan=lifespan,
    servers=[
        {"url": "http://localhost:8000", "description": "local environment"},
    ],
)

app.include_router(api_router)
