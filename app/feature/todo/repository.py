from datetime import datetime
from uuid import UUID

from domain.todo.model import Todo
from domain.todo.repository import TodoRepository
from sqlmodel import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession


class TodoRepositoryImpl(TodoRepository[AsyncSession]):
    async def create(self, todo: Todo) -> None:
        self.session.add(todo)
        await self.session.commit()
        await self.session.refresh(todo)

    async def find_all(self) -> list[Todo]:
        statement = select(Todo)
        results = await self.session.exec(statement=statement)
        items = results.all()
        return items

    async def find_by_id(self, id: UUID) -> Todo | None:
        statement = select(Todo).where(Todo.id == id)
        results = await self.session.exec(statement=statement)
        item = results.first()
        return item

    async def update(self, id: UUID, todo: Todo) -> None:
        item = await self.find_by_id(id=id)
        if item is None:
            return
        values = todo.model_dump(exclude_unset=True)
        for k, v in values.items():
            setattr(item, k, v)
        item.updated_at = datetime.utcnow()
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)

    async def delete(self, id: UUID) -> None:
        statement = delete(Todo).where(Todo.id == id)

        await self.session.exec(statement=statement)
        await self.session.commit()
