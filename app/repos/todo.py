from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.todo import Todo, TodoCreate, TodoPatch


class TodoCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: TodoCreate) -> Todo:
        values = data.model_dump()
        item = Todo(**values)
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)

        return item

    async def read(self) -> list[Todo]:
        statement = select(Todo)
        results = await self.session.exec(statement=statement)
        items: list[Todo] = results.all()

        return items

    async def get(self, todo_id: str | UUID) -> Todo:
        statement = select(Todo).where(Todo.id == todo_id)
        results = await self.session.exec(statement=statement)
        item: Todo | None = results.scalar_one_or_none()

        if item is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
            )

        return item

    async def patch(self, todo_id: str | UUID, data: TodoPatch) -> Todo:
        item = await self.get(todo_id=todo_id)
        values = data.model_dump(exclude_unset=True)

        for k, v in values.items():
            setattr(item, k, v)

        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)

        return item

    async def delete(self, todo_id: str | UUID) -> bool:
        statement = delete(Todo).where(Todo.id == todo_id)

        await self.session.exec(statement=statement)
        await self.session.commit()

        return True
