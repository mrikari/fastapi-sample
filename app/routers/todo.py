from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Path
from models.todo import TodoAbst, TodoCreate, TodoPatch
from services.todo import ServiceFactory, TodoService

# request parameter/body annotated
BodyTodoCreate = Annotated[TodoCreate, Body(..., title="Todo Data")]
BodyTodoPatch = Annotated[TodoPatch, Body(..., title="Todo Data")]
PathID = Annotated[UUID, Path(..., title="ID")]

router = APIRouter()


@router.get(
    "",
    summary="TODO一覧取得",
    description="登録されたTODOの一覧を返却する。",
    response_model=list[TodoAbst],
)
async def get_todos(service: Annotated[TodoService, Depends(ServiceFactory())]):
    result = await service.get_todo_list()
    return result


@router.post(
    "",
    summary="TODO登録",
    description="TODOを登録する。",
    response_model=TodoCreate,
)
async def create_todo_item(
    service: Annotated[TodoService, Depends(ServiceFactory())],
    body: BodyTodoCreate,
):
    return await service.create_todo(
        title=body.title,
        flg=body.is_complete,
    )


@router.get(
    "/{id}",
    summary="TODO情報取得",
    description="指定されたTODOを返却する。",
)
async def get_todo_item(
    service: Annotated[TodoService, Depends(ServiceFactory())],
    id: PathID,
):
    result = await service.get_todo(id)
    return result


@router.delete(
    "/{id}",
    summary="TODO情報削除",
    description="指定されたTODOを削除する。",
)
async def delete_todo_item(
    service: Annotated[TodoService, Depends(ServiceFactory())],
    id: PathID,
) -> bool:
    return await service.delete_todo(id)


@router.patch(
    "/{id}",
    summary="TODO情報更新",
    description="指定されたTODOを更新する。",
    response_model=TodoPatch,
)
async def delete_todo_item(
    service: Annotated[TodoService, Depends(ServiceFactory())],
    id: PathID,
    body: BodyTodoPatch,
):
    result = await service.patch_todo(id, title=body.title, flg=body.is_complete)
    return result


@router.post(
    "/{id}/complete",
    summary="TODO完了",
    description="指定されたTODOを完了にする。",
    response_model=TodoPatch,
)
async def change_complete_todo_item(
    service: Annotated[TodoService, Depends(ServiceFactory())],
    id: PathID,
):
    result = await service.set_complete(id)
    return result


@router.post(
    "/{id}/incomplete",
    summary="TODO未完了",
    description="指定されたTODOを未完了にする。",
    response_model=TodoPatch,
)
async def change_incomplete_todo_item(
    service: Annotated[TodoService, Depends(ServiceFactory())],
    id: PathID,
):
    result = await service.set_incomplete(id)
    return result
