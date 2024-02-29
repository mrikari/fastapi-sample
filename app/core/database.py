from typing import Annotated

from core.config import get_db_settings
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

_settings = get_db_settings()

async_engine = create_async_engine(
    _settings.DATABASE_DSN.unicode_string(),
    echo=_settings.ECHO_STATEMENT,  # show query statement
    future=True,
)


async def get_async_session() -> AsyncSession:  # type: ignore
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session


DBSession = Annotated[AsyncSession, Depends(get_async_session)]


def create_all():
    SQLModel.metadata.create_all(async_engine)
