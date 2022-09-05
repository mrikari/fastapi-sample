from datetime import datetime

from pydantic import BaseModel


class TodoItem(BaseModel):
    title: str
    is_complete: bool


class Todo(TodoItem):
    id: int
    created_at: datetime
    updated_at: datetime


class CreateTodo(TodoItem):
    pass
