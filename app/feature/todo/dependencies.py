from typing import Annotated

from core.database import get_async_session
from domain.todo.repository import TodoRepository
from domain.todo.service import TodoService
from fastapi import Depends
from feature.todo.repository import TodoRepositoryImpl
from feature.todo.service import TodoServiceImpl
from sqlmodel.ext.asyncio.session import AsyncSession


def get_todo_repository(
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> TodoRepository:
    return TodoRepositoryImpl(session)


def get_todo_service(
    repo: Annotated[TodoRepository, Depends(get_todo_repository)]
) -> TodoService:
    return TodoServiceImpl(repo)
