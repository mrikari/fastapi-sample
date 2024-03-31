import uuid
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from domain.todo.model import Todo
from feature.todo.repository import TodoRepositoryImpl as TodoRepository
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession


@pytest_asyncio.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """テスト用の非同期エンジンとsessionmakerを作成します

    Yields:
        AsyncSession: 非同期セッション
    """
    DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/test_sample"
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    async_sessionmaker = sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )
    async with async_sessionmaker() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
    await engine.dispose()


@pytest.mark.asyncio
async def test_save_and_get_todo(db_session: AsyncSession):
    """TODOを保存して取得するテスト

    Args:
        db_session (AsyncSession): 非同期セッション
    """
    todo_repository = TodoRepository(session=db_session)
    todo_id = uuid.uuid4()
    item = Todo(
        id=todo_id,
        title="test",
        is_complete=False,
    )
    await todo_repository.create(item)
    retrieved_todo = await todo_repository.find_by_id(todo_id)

    assert retrieved_todo.id == todo_id
    assert retrieved_todo.title == "test"


@pytest.mark.asyncio
async def test_list_todo(db_session: AsyncSession):
    """TODOを保存して一括取得するテスト

    Args:
        db_session (AsyncSession): 非同期セッション
    """
    todo_repository = TodoRepository(session=db_session)
    todo1_id = uuid.uuid4()
    item1 = Todo(
        id=todo1_id,
        title="test",
        is_complete=False,
    )
    todo2_id = uuid.uuid4()
    item2 = Todo(
        id=todo2_id,
        title="test",
        is_complete=False,
    )
    await todo_repository.create(item1)
    await todo_repository.create(item2)
    todo_repository = TodoRepository(session=db_session)
    retrieved_todo = await todo_repository.find_all()

    assert len(retrieved_todo) == 2


@pytest.mark.asyncio
async def test_delete_todo(db_session: AsyncSession):
    """保存したTODOを削除するテスト

    Args:
        db_session (AsyncSession): 非同期セッション
    """
    todo_repository = TodoRepository(session=db_session)
    todo_id = uuid.uuid4()
    item = Todo(
        id=todo_id,
        title="test",
        is_complete=False,
    )
    await todo_repository.create(item)
    retrieved_todo = await todo_repository.find_by_id(todo_id)

    assert retrieved_todo.id == todo_id
    assert retrieved_todo.title == "test"

    await todo_repository.delete(todo_id)
    retrieved_todo = await todo_repository.find_by_id(todo_id)

    assert retrieved_todo is None


@pytest.mark.asyncio
async def test_update_todo(db_session: AsyncSession):
    """保存したTODOを更新するテスト

    Args:
        db_session (AsyncSession): 非同期セッション
    """
    todo_repository = TodoRepository(session=db_session)
    todo_id = uuid.uuid4()
    item = Todo(
        id=todo_id,
        title="test",
        is_complete=False,
    )
    await todo_repository.create(item)
    retrieved_todo = await todo_repository.find_by_id(todo_id)

    assert retrieved_todo.id == todo_id
    assert retrieved_todo.title == "test"
    assert retrieved_todo.is_complete == False

    await todo_repository.update(todo_id, Todo(title="update", is_complete=True))

    retrieved_todo = await todo_repository.find_by_id(todo_id)

    assert retrieved_todo.id == todo_id
    assert retrieved_todo.title == "update"
    assert retrieved_todo.is_complete == True


@pytest.mark.asyncio
async def test_update_not_exsits_todo(db_session: AsyncSession):
    """存在しないTODOを更新するテスト

    Args:
        db_session (AsyncSession): 非同期セッション
    """
    todo_repository = TodoRepository(session=db_session)
    todo_id = uuid.uuid4()
    res = await todo_repository.update(
        todo_id, Todo(id=todo_id, title="not update", is_complete=False)
    )
    retrieved_todo = await todo_repository.find_by_id(todo_id)

    assert retrieved_todo is None
    assert res is None
