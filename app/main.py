from fastapi import FastAPI

from dependencies import get_settings
from events import shutdown, startup
from routers import root, todo

conf = get_settings()


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
    routes=[*root.router_v2.routes, *app1.router.routes],
)

app3 = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=[*root.router_v3.routes, *app2.router.routes],
)

app = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=app3.routes,
)

app.mount('/v1', app1)
app.mount('/v2', app2)
app.mount('/v3', app3)
