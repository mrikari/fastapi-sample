from core.config import settings
from fastapi import FastAPI
from routers import root, todo

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.description,
    debug=settings.debug,
)

app.include_router(root.router)
app.include_router(todo.router)
