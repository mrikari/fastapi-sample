import logging
from typing import Annotated

from core.config import Settings, get_logger, get_settings
from core.models import HealthCheck
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()
logger = get_logger()


@router.get("/")
def root():
    return JSONResponse(content={"message": "It works!"})


@router.get("/health")
def get_healthcheck(settings: Annotated[Settings, Depends(get_settings)]):
    return HealthCheck(
        name=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
    )


@router.get("/loglevel", include_in_schema=False)
def get_log_level():
    logger.debug(f"loglevel: {logging.DEBUG}")
    logger.info(f"loglevel: {logging.INFO}")
    logger.warn(f"loglevel: {logging.WARN}")
    logger.error(f"loglevel: {logging.ERROR}")
    logger.critical(f"loglevel: {logging.CRITICAL}")
    return JSONResponse(content={"level": logging.getLevelName(logger.level)})
