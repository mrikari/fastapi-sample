from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from core.models import TimestampModel, UUIDModel


class TodoBase(SQLModel):
    title: str = Field("", title="タイトル", min_length=1)
    is_complete: bool = Field(False, title="完了")


class Todo(TimestampModel, TodoBase, UUIDModel, table=True):
    __tablename__ = "todos"


### Response Models ###


class TodoCreate(TodoBase): ...


class TodoRead(BaseModel):
    list: list[Todo]


class TodoPatch(TodoBase):
    title: Optional[str] = Field(None, title="タイトル", min_length=1)
    is_complete: Optional[bool] = Field(None, title="完了")
