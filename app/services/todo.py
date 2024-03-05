from abc import ABC, abstractclassmethod
from typing import Annotated, Literal
from uuid import UUID, uuid4

from fastapi import Depends
from models.todo import Todo
from repositories.todo import RepositoryFactory, TodoRepository


class TodoService(ABC):
    repo: TodoRepository

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


class TodoServiceImpl(TodoService):
    def __init__(self, repo: TodoRepository) -> None:
        self.repo = repo

    async def get_todo_list(self):
        items = await self.repo.retrieve()
        return items

    async def get_todo(self, id):
        items = await self.repo.retrieve(id=id)
        if len(items) == 0:
            return None
        return items[0]

    async def create_todo(self, title: str, flg: bool):
        item = Todo(title=title, is_complete=flg)
        await self.repo.create(todo=item)
        return item

    async def delete_todo(self, id):
        await self.repo.delete(id)
        return True

    async def patch_todo(self, id, title: str, flg: bool):
        update_field = Todo()
        if title:
            update_field.title = title
        if flg is not None:
            update_field.is_complete = flg
        await self.repo.update(id, update_field)
        items = await self.repo.retrieve(id=id)
        return items[0]

    async def set_complete(self, id):
        update_field = Todo(is_complete=True)
        await self.repo.update(id, update_field)
        items = await self.repo.retrieve(id=id)
        return items[0]

    async def set_incomplete(self, id):
        update_field = Todo(is_complete=False)
        await self.repo.update(id, update_field)
        items = await self.repo.retrieve(id=id)
        return items[0]


class TodoServiceMock(TodoService):
    def __init__(self, repo: TodoRepository) -> None:
        self.repo = repo

    async def get_todo_list(self) -> list[Todo]:
        return [
            Todo(id=uuid4(), title="mock1", is_complete=False),
            Todo(id=uuid4(), title="mock2", is_complete=False),
            Todo(id=uuid4(), title="mock3", is_complete=True),
        ]

    async def get_todo(self, id) -> Todo:
        return Todo(id=uuid4(), title="mock", is_complete=False)

    async def create_todo(self, title: str, flg: bool) -> Todo:
        return Todo(id=uuid4(), title=title, is_complete=flg)

    async def delete_todo(self, id): ...
    async def patch_todo(self, id, title: str, flg: bool) -> Todo:
        return Todo(id=uuid4(), title="mock-patch", is_complete=True)

    async def set_complete(self, id): ...
    async def set_incomplete(self, id): ...


class ServiceFactory:
    def __init__(self, type: Literal["impl", "mock"] = "impl") -> None:
        self._type = type

    def __call__(
        self,
        repo: Annotated[TodoRepository, Depends(RepositoryFactory(type="asyncdb"))],
    ):
        if self._type == "impl":
            return TodoServiceImpl(repo)
        elif self._type == "mock":
            return TodoServiceMock(repo)
        else:
            return TodoServiceImpl(repo)
