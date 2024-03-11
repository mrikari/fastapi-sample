import asyncio
from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import pytest
from domain.todo.model import Todo
from feature.todo.repository import TodoRepositoryImpl
from sqlmodel.sql.expression import SelectOfScalar


@pytest.mark.asyncio
async def test_select_all():
    rand_uuid = uuid4()
    rand_uuid2 = uuid4()
    mock_result = MagicMock()
    mock_result.all.return_value = [
        Todo(id=rand_uuid, title="test1", is_complete=False),
        Todo(id=rand_uuid2, title="test2", is_complete=False),
    ]
    mock_db = AsyncMock(return_value=asyncio.Future())
    mock_db.exec.return_value = mock_result
    repo = TodoRepositoryImpl(session=mock_db)
    result = await repo.find_all()
    statement = mock_db.exec.call_args.kwargs["statement"]
    # execされるstatementはTodoのSelectOfScalarであること
    assert isinstance(statement, SelectOfScalar[Todo])
    # exec結果は未加工であること
    assert result[0].id == rand_uuid
    assert result[1].id == rand_uuid2
