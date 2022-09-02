from functools import lru_cache
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from config.settings import Settings

conf = Settings()
app = FastAPI(
    title=conf.app_name,
    version=conf.app_version,
    debug=conf.debug,
)


@lru_cache()
def get_settings():
    return Settings()


@app.get('/')
def root():
    return JSONResponse(content={'message': 'It works!'})


@app.get('/info')
def get_info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
    }
