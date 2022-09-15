from config.settings import Settings
from dependencies import get_settings
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(prefix="", tags=["Root"])


@router.get("/")
def root():
    return JSONResponse(content={"message": "It works!"})


@router.get("/info")
def get_info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
    }
