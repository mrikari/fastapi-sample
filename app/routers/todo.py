from fastapi import APIRouter, Body, Path
from models.todo import CreateTodo, CreateTodoResult, Todo
from services.todo import (
    create_todo,
    delete_todo,
    read_todo,
    read_todo_list,
    update_complete,
)

router = APIRouter(prefix="/todos", tags=["Todo"])


@router.get(
    "",
    summary="TODO一覧取得",
    description="登録されたTODOの一覧を返却する。",
    response_model=list[Todo],
)
async def get_todos():
    return await read_todo_list()


@router.post(
    "",
    summary="TODO登録",
    description="TODOを登録する。",
    response_model=CreateTodoResult,
)
async def create_todo_item(body: CreateTodo = Body(..., title="Todo Data")):
    return await create_todo(body.title, is_complete=body.is_complete)


@router.get(
    "/{id}",
    summary="TODO情報取得",
    description="指定されたTODOを返却する。",
)
async def get_todo_item(id: int = Path(..., title="ID")):
    return await read_todo(id)


@router.delete(
    "/{id}",
    summary="TODO情報削除",
    description="指定されたTODOを削除する。",
)
async def delete_todo_item(id: int = Path(..., title="ID")):
    return await delete_todo(id)


@router.post(
    "/{id}/complete",
    summary="TODO完了",
    description="指定されたTODOを完了にする。",
)
async def change_complete_todo_item(id: int = Path(..., title="ID")):
    return await update_complete(id, True)


@router.post(
    "/{id}/incomplete",
    summary="TODO未完了",
    description="指定されたTODOを未完了にする。",
)
async def change_incomplete_todo_item(id: int = Path(..., title="ID")):
    return await update_complete(id, False)
