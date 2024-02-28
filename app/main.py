from core.config import get_settings
from fastapi import FastAPI
from routers import root, todo

_settings = get_settings()
app = FastAPI(
    title=_settings.APP_NAME,
    version=_settings.APP_VERSION,
    description=_settings.APP_DESCRIPTION,
    debug=_settings.DEBUG,
)

app.include_router(root.router)
app.include_router(todo.router)
