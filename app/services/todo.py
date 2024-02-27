from typing import Optional
from uuid import UUID

from models.todo import Todo, TodoCreate, TodoPatch
from cruds.todo import TodoCRUD
from sqlmodel import Session


async def read_todo_list(session: Session) -> list[Todo]:
    """"""
    todo = TodoCRUD(session=session)
    return await todo.read()


async def read_todo(session: Session, id: str | UUID) -> Todo:
    """"""
    todo = TodoCRUD(session=session)
    return await todo.get(todo_id=id)


async def create_todo(session: Session, title: str, is_complete: bool = False) -> Todo:
    """"""
    todo = TodoCRUD(session=session)
    return await todo.create(data=TodoCreate(title=title, is_complete=is_complete))


async def delete_todo(session: Session, id: str | UUID) -> bool:
    """"""
    todo = TodoCRUD(session=session)
    return await todo.delete(todo_id=id)


async def patch_todo(
    session: Session,
    id: str | UUID,
    title: Optional[str] = None,
    flg: Optional[bool] = None,
) -> Todo:
    """"""
    todo = TodoCRUD(session=session)
    return await todo.patch(
        todo_id=id, data=TodoPatch(title=title, is_complete=flg), exclude_none=True
    )
