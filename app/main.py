from dependencies import get_settings
from events import shutdown, startup
from fastapi import FastAPI
from routers import root, todo

conf = get_settings()

app = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
    on_startup=[startup],
    on_shutdown=[shutdown],
)

app.include_router(root.router)
app.include_router(todo.router)
