from typing import Optional

from core.models import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    title: str = Field("", title="タイトル", min_length=1)
    is_complete: bool = Field(False, title="完了")


class Todo(TimestampModel, TodoBase, UUIDModel, table=True):
    __tablename__ = "todos"


### Response Models ###


class TodoCreate(TodoBase): ...


class TodoRead(UUIDModel, TodoBase): ...


class TodoPatch(TodoBase):
    title: Optional[str] = Field(None, title="タイトル", min_length=1)
    is_complete: Optional[bool] = Field(None, title="完了")
