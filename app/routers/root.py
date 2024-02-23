from typing import Annotated

from core.config import Settings, get_settings
from core.models import HealthCheck
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(prefix="", tags=["Root"])


@router.get("/")
def root():
    return JSONResponse(content={"message": "It works!"})


@router.get("/health")
def get_healthcheck(settings: Annotated[Settings, Depends(get_settings)]):
    return HealthCheck(
        name=settings.app_name,
        version=settings.app_version,
        description=settings.description,
    )
