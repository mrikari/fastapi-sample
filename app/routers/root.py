from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from config.settings import Settings
from dependencies import get_settings

router = APIRouter(prefix="", tags=["Root"])
router_v2 = APIRouter(prefix="", tags=["Root"])
router_v3 = APIRouter(prefix="", tags=["Root"])


@router.get("/")
def root():
    return JSONResponse(content={"message": "It works!"})


@router.get("/info")
def get_info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
    }


@router_v2.get("/")
def root():
    return JSONResponse(content={"message": "It v2 works!"})


@router_v2.get("/info")
def get_info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
    }


@router_v3.get("/")
def root():
    return JSONResponse(content={"message": "It v3 works!"})


@router_v3.get("/info")
def get_info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
    }