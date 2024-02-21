from core.models import HealthCheck
from core.config import settings
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="", tags=["Root"])


@router.get("/")
def root():
    print(settings)
    return JSONResponse(content={"message": "It works!"})


@router.get("/health")
def get_healthcheck():
    return HealthCheck(
        name=settings.app_name,
        version=settings.app_version,
        description=settings.description,
    )
