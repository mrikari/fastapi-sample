from fastapi.exceptions import HTTPException
from database import database
from models.todo import (
    CreateTodoResult,
    DeleteTodoResult,
    Todo,
    UpdateTodoResult,
)
from schemas.todo import todos
from sqlalchemy import delete, insert, select, update


async def read_todo_list() -> list[Todo]:
    """"""
    stmt = select(todos)
    result: list[Todo] = await database.fetch_all(stmt)
    return result


async def read_todo(id: int) -> Todo:
    """"""
    stmt = select(todos).where(todos.c.id == id)
    result: Todo = await database.fetch_one(stmt)
    if result is None:
        raise HTTPException(status_code=404)
    return result


async def create_todo(
    title: str, is_complete: bool = False
) -> CreateTodoResult:
    """"""
    stmt = insert(todos).values(title=title, is_complete=is_complete)
    pk: int = await database.execute(stmt)
    return CreateTodoResult(id=pk)


async def delete_todo(id: int) -> DeleteTodoResult:
    """"""
    stmt = delete(todos).where(todos.c.id == id)
    result: int = await database.execute(stmt)
    if result == 0:
        raise HTTPException(status_code=404)
    return DeleteTodoResult(count=result)


async def update_complete(id: int, flg: bool) -> UpdateTodoResult:
    """"""
    stmt = update(todos).where(todos.c.id == id).values(is_complete=flg)
    result: int = await database.execute(stmt)
    if result == 0:
        raise HTTPException(status_code=404)
    return UpdateTodoResult(count=result)
