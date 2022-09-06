from sqlalchemy import delete, insert, select, update

from database import database
from models.todo import (CreateTodoResult, DeleteTodoResult, Todo,
                         UpdateTodoResult)
from schemas.todo import todos


async def read_todo_list() -> list[Todo]:
    """"""
    stmt = select(todos)
    result: list[Todo] = await database.fetch_all(stmt)
    return result


async def read_todo_list_v2(limit: int = None, offset: int = 0) -> list[Todo]:
    """"""
    stmt = select(todos).limit(limit).offset(offset)
    result: list[Todo] = await database.fetch_all(stmt)
    return result


async def read_todo(id: int) -> Todo:
    """"""
    stmt = select(todos).where(todos.c.id == id)
    result: Todo = await database.fetch_one(stmt)
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
    return DeleteTodoResult(count=result)


async def update_complete(id: int, flg: bool) -> UpdateTodoResult:
    """"""
    stmt = update(todos).where(todos.c.id == id).values(is_complete=flg)
    result: int = await database.execute(stmt)
    return UpdateTodoResult(count=result)
