import asyncio
import os
from json import loads
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel
import domain.models  # noqa: 'autogenerate' support

from core.config import get_db_settings

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

target_metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)" "s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
exclude_tables = loads(os.getenv("DB_EXCLUDE_TABLES", "{}"))


def filter_db_objects(
    object,  # noqa: indirect usage
    name,
    type_,
    *args,  # noqa: indirect usage
    **kwargs,  # noqa: indirect usage
):
    if type_ == "table":
        return name not in exclude_tables

    if type_ == "index" and name.startswith("idx") and name.endswith("geom"):
        return False

    return True


def run_migrations_offline() -> None:
    url = get_db_settings().DATABASE_DSN.unicode_string()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    config_section = config.get_section(config.config_ini_section)
    url = get_db_settings().DATABASE_DSN.unicode_string()
    config_section["sqlalchemy.url"] = url

    connectable = AsyncEngine(
        engine_from_config(
            config_section,
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


async def run_migrations_online() -> None:
    config_section = config.get_section(config.config_ini_section)
    url = get_db_settings().DATABASE_DSN.unicode_string()
    config_section["sqlalchemy.url"] = url

    connectable = AsyncEngine(
        engine_from_config(
            config_section,
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
