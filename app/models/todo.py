from datetime import datetime

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    title: str
    is_complete: bool


class Todo(TodoItem):
    id: int
    created_at: datetime
    updated_at: datetime


class CreateTodo(TodoItem):
    pass


class CreateTodoResult(BaseModel):
    id: int = Field(None, title="追加したTodoのID")


class DeleteTodoResult(BaseModel):
    count: int = Field(None, title="削除したTodo数")


class UpdateTodoResult(BaseModel):
    count: int = Field(None, title="更新したTodo数")
