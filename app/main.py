from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse

from config.settings import Settings
from database import database
from dependencies import get_settings
from routers import todo

conf = get_settings()
app = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def root():
    return JSONResponse(content={"message": "It works!"})


@app.get("/info")
def get_info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
    }


app.include_router(todo.router)
