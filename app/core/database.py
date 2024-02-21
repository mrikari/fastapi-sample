from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from core.config import settings

async_engine = create_async_engine(
    settings.database_dsn.unicode_string(), echo=True, future=True
)

async def get_async_session() -> AsyncSession: # type: ignore
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


def create_all():
    SQLModel.metadata.create_all(async_engine)
