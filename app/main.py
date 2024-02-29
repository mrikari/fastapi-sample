from logging import getLogger

from core.config import get_settings
from fastapi import FastAPI
from routers import root, todo

logger = getLogger("uvicorn")

_settings = get_settings()


def lifespan(app: FastAPI):
    logger.setLevel(_settings.LOG_LEVEL)
    logger.debug(f"docs_url -> {app.docs_url}")
    logger.debug(f"redoc_url -> {app.redoc_url}")
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

app.include_router(root.router)
app.include_router(todo.router)
