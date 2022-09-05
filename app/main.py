from fastapi import FastAPI

from events import startup, shutdown
from dependencies import get_settings
from routers import todo, root


conf = get_settings()

app = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=[*todo.router.routes, *root.router_v3.routes],
)

app1 = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=[*todo.router.routes, *root.router.routes],
)

app2 = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=[*todo.router.routes, *root.router_v2.routes],
)

app3 = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=[*todo.router.routes, *root.router_v3.routes],
)

app.mount('/v1', app1)
app.mount('/v2', app2)
app.mount('/v3', app3)
