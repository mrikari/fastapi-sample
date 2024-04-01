import uuid
import pytest
from domain.todo.model import Todo
from feature.todo.repository import TodoRepositoryImpl as TodoRepository
from feature.todo.service import TodoServiceImpl as TodoService
from unittest.mock import MagicMock


@pytest.fixture
def test_repository() -> TodoRepository:
    repository_mock = MagicMock(spec=TodoRepository)
    repository_mock.create.return_value = None
    repository_mock.delete.return_value = None
    repository_mock.find_all.return_value = [
        Todo(title="mock1", is_complete=False),
        Todo(title="mock2", is_complete=False),
    ]
    repository_mock.find_by_id.return_value = Todo(title="mock", is_complete=False)
    repository_mock.update.return_value = None
    return repository_mock


@pytest.mark.asyncio
async def test_create_service(test_repository: TodoRepository):
    """渡したパラメータをTODOのモデルにしてcreateリポジトリが呼ばれることの検証

    Args:
        test_repository (TodoRepository): _description_
    """
    service = TodoService(repo=test_repository)
    item = await service.create_todo(title="test", flg=False)

    # リポジトリのcreateが呼ばれていること
    test_repository.create.assert_called()

    # 引数の型が一致するか検証
    _, kwargs = test_repository.create.call_args
    assert isinstance(kwargs["todo"], Todo)
    assert kwargs["todo"].title == "test"
    assert kwargs["todo"].is_complete == False

    # 返り値はTodoであること
    assert isinstance(item, Todo)


@pytest.mark.asyncio
async def test_delete_service(test_repository: TodoRepository):
    """削除されるTODOのIDが適切に指定されていることの検証

    Args:
        test_repository (TodoRepository): _description_
    """
    service = TodoService(repo=test_repository)
    todo_id = uuid.uuid4()
    item = await service.delete_todo(id=todo_id)

    # リポジトリのcreateが呼ばれていること
    test_repository.delete.assert_called()

    # 引数の型が一致するか検証
    _, kwargs = test_repository.delete.call_args
    assert kwargs["id"] == todo_id

    # 返り値はTodoであること
    assert item == True


@pytest.mark.asyncio
async def test_get_service(test_repository: TodoRepository):
    """指定したIDのTODOが取得できることの検証

    Args:
        test_repository (TodoRepository): _description_
    """
    service = TodoService(repo=test_repository)
    todo_id = uuid.uuid4()
    item = await service.get_todo(id=todo_id)

    # リポジトリのcreateが呼ばれていること
    test_repository.find_by_id.assert_called()

    # 引数の型が一致するか検証
    _, kwargs = test_repository.find_by_id.call_args
    assert kwargs["id"] == todo_id

    # 返り値はTodoであること
    assert item.title == "mock"


@pytest.mark.asyncio
async def test_list_service(test_repository: TodoRepository):
    """TODOリストが取得できることの検証

    Args:
        test_repository (TodoRepository): _description_
    """
    service = TodoService(repo=test_repository)
    item = await service.get_todo_list()

    # リポジトリのcreateが呼ばれていること
    test_repository.find_all.assert_called()

    # 返り値はTodoであること
    assert item[0].title == "mock1"
