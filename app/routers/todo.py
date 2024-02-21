from uuid import UUID
from fastapi import APIRouter, Body, Depends, Path
from sqlmodel import Session
from core.database import get_async_session
from models.todo import TodoCreate, TodoPatch, TodoRead
from services.todo import (
    create_todo,
    delete_todo,
    patch_todo,
    read_todo,
    read_todo_list,
)

router = APIRouter(prefix="/todos", tags=["Todo"])


@router.get(
    "",
    summary="TODO一覧取得",
    description="登録されたTODOの一覧を返却する。",
    response_model=TodoRead,
)
async def get_todos(session: Session = Depends(get_async_session)):
    result = await read_todo_list(session=session)
    return TodoRead(list=result)

@router.post(
    "",
    summary="TODO登録",
    description="TODOを登録する。",
    response_model=TodoCreate,
)
async def create_todo_item(
    session: Session = Depends(get_async_session),
    body: TodoCreate = Body(..., title="Todo Data"),
):
    return await create_todo(session, body.title, is_complete=body.is_complete)


@router.get(
    "/{id}",
    summary="TODO情報取得",
    description="指定されたTODOを返却する。",
)
async def get_todo_item(
    session: Session = Depends(get_async_session),
    id: UUID = Path(..., title="ID"),
):
    return await read_todo(session, id)


@router.delete(
    "/{id}",
    summary="TODO情報削除",
    description="指定されたTODOを削除する。",
)
async def delete_todo_item(
    session: Session = Depends(get_async_session),
    id: UUID = Path(..., title="ID"),
) -> bool:
    return await delete_todo(session, id)


@router.patch(
    "/{id}",
    summary="TODO情報更新",
    description="指定されたTODOを更新する。",
    response_model=TodoPatch,
)
async def delete_todo_item(
    session: Session = Depends(get_async_session),
    id: UUID = Path(..., title="ID"),
    body: TodoPatch = Body(..., title="Todo Data"),
):
    return await patch_todo(
        session,
        id,
        title=body.title,
        flg=body.is_complete,
    )


@router.post(
    "/{id}/complete",
    summary="TODO完了",
    description="指定されたTODOを完了にする。",
    response_model=TodoPatch,
)
async def change_complete_todo_item(
    session: Session = Depends(get_async_session),
    id: UUID = Path(..., title="ID"),
):
    return await patch_todo(session, id, flg=True)


@router.post(
    "/{id}/incomplete",
    summary="TODO未完了",
    description="指定されたTODOを未完了にする。",
    response_model=TodoPatch,
)
async def change_incomplete_todo_item(
    session: Session = Depends(get_async_session),
    id: UUID = Path(..., title="ID"),
):
    return await patch_todo(session, id, flg=False)
