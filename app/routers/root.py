from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from config.settings import Settings
from dependencies import get_settings
from routers import override_route

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


# routerV2 settings


router_v2 = APIRouter(prefix="", tags=["Root"])

# Override


@router_v2.get("/")
def root_v2():
    return JSONResponse(content={"message": "It v2 works!"})


# Inheritance V1
router_v2.routes += override_route(router.routes, router_v2.routes)

# routerV3 settings

router_v3 = APIRouter(prefix="", tags=["Root"])

# Override


@router_v3.get("/")
def root_v3():
    return JSONResponse(content={"message": "It v3 works!"})


# Inheritance V2
router_v3.routes += override_route(router_v2.routes, router_v3.routes)
