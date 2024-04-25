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
        await self.repo.delete(id=id)
        return True

    async def patch_todo(self, id, title: str, flg: bool):
        update_field = Todo()
        if title:
            update_field.title = title
        if flg is not None:
            update_field.is_complete = flg
        await self.repo.update(id=id, entity=update_field)
        item = await self.repo.find_by_id(id=id)
        return item

    async def set_complete(self, id):
        update_field = Todo(is_complete=True)
        await self.repo.update(id=id, entity=update_field)
        item = await self.repo.find_by_id(id=id)
        return item

    async def set_incomplete(self, id):
        update_field = Todo(is_complete=False)
        await self.repo.update(id=id, entity=update_field)
        item = await self.repo.find_by_id(id=id)
        return item
