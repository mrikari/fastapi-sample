from datetime import datetime

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    title: str = Field("", title="タイトル", min_length=1)
    is_complete: bool = Field(False, title="完了")


class Todo(TodoItem):
    id: int = Field(..., title="ID")
    created_at: datetime = Field(..., title="作成日時")
    updated_at: datetime = Field(..., title="更新日時")


class CreateTodo(TodoItem):
    pass


class CreateTodoResult(BaseModel):
    id: int = Field(None, title="追加したTodoのID")


class DeleteTodoResult(BaseModel):
    count: int = Field(None, title="削除したTodo数")


class UpdateTodoResult(BaseModel):
    count: int = Field(None, title="更新したTodo数")
