from uuid import uuid4

from domain.todo.model import Todo
from domain.todo.service import TodoService
from feature.todo.repository import TodoRepository


class TodoServiceImpl(TodoService[TodoRepository]):
    async def get_todo_list(self):
        items = await self.repo.find_all()
        return items

    async def get_todo(self, id):
        item = await self.repo.find_by_id(id=id)
        return item

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
        item = await self.repo.find_by_id(id=id)
        return item

    async def set_complete(self, id):
        update_field = Todo(is_complete=True)
        await self.repo.update(id, update_field)
        item = await self.repo.find_by_id(id=id)
        return item

    async def set_incomplete(self, id):
        update_field = Todo(is_complete=False)
        await self.repo.update(id, update_field)
        item = await self.repo.find_by_id(id=id)
        return item


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
