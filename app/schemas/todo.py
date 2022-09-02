from sqlalchemy import Boolean, Column, DateTime, Integer, String, Table
from sqlalchemy.sql.functions import current_timestamp

from database import metadata

todos = Table(
    "Todos",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String(128), nullable=False),
    Column("is_complete", Boolean, default=False, nullable=False),
    Column(
        "created_at",
        DateTime,
        nullable=False,
        server_default=current_timestamp(),
    ),
    Column(
        "updated_at",
        DateTime,
        nullable=False,
        server_default=current_timestamp(),
    ),
)
