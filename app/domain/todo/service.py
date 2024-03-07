from abc import ABC, abstractclassmethod
from typing import Generic, TypeVar
from uuid import UUID

from domain.todo.model import Todo

AnyRepo = TypeVar("AnyRepo")


class TodoService(ABC, Generic[AnyRepo]):
    def __init__(self, repo: AnyRepo) -> None:
        self.repo = repo

    @abstractclassmethod
    async def get_todo_list(self) -> list[Todo]: ...
    @abstractclassmethod
    async def get_todo(self, id: UUID) -> Todo | None: ...
    @abstractclassmethod
    async def create_todo(self, title: str, flg: bool) -> Todo: ...
    @abstractclassmethod
    async def delete_todo(self, id: UUID) -> bool: ...
    @abstractclassmethod
    async def patch_todo(
        self, id, title: str | None = None, flg: bool | None = None
    ) -> Todo: ...
    @abstractclassmethod
    async def set_complete(self, id: UUID) -> Todo: ...
    @abstractclassmethod
    async def set_incomplete(self, id: UUID) -> Todo: ...
