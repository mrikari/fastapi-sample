from abc import ABC, abstractclassmethod
from datetime import datetime
from typing import Any, Generic, Literal, TypeVar
from uuid import UUID

from core.database import DBSession
from models.todo import Todo
from sqlmodel import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession

AnySession = TypeVar("AnySession")


class TodoRepository(ABC, Generic[AnySession]):
    def __init__(self, session: AnySession) -> None:
        """非同期DBセッション

        Args:
            session (AsyncSession): _description_
        """
        self.session = session

    @abstractclassmethod
    async def create(self, todo: Todo):
        """TodoのテーブルにCREATEクエリを発行する

        Args:
            todo (Todo): _description_
        """

    @abstractclassmethod
    async def retrieve(self, id: UUID | None) -> list[Todo]:
        """_summary_

        Args:
            id (UUID | None): _description_

        Returns:
            list[Todo]: _description_
        """

    @abstractclassmethod
    async def update(self, id: UUID, todo: Todo):
        """_summary_

        Args:
            id (UUID): _description_
            todo (Todo): _description_
        """

    @abstractclassmethod
    async def delete(self, id: UUID):
        """_summary_

        Args:
            id (UUID): _description_

        Returns:
            _type_: _description_
        """


class TodoRepositoryImpl(TodoRepository[AsyncSession]):
    async def create(self, todo: Todo) -> None:
        self.session.add(todo)
        await self.session.commit()
        await self.session.refresh(todo)

    async def retrieve(self, id: UUID | None = None) -> list[Todo]:
        statement = select(Todo)
        if id:
            statement = statement.where(Todo.id == id)
        results = await self.session.exec(statement=statement)
        items = results.all()
        return items

    async def update(self, id: UUID, todo: Todo) -> None:
        items = await self.retrieve(id=id)
        if len(items) == 0:
            return
        item = items[0]
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


class RepositoryFactory:
    def __init__(self, type: Literal["asyncdb"] = "asyncdb") -> None:
        self._type = type

    def __call__(self, session: DBSession) -> Any:
        if self._type == "asyncdb":
            return TodoRepositoryImpl(session)
        else:
            return TodoRepositoryImpl(session)
