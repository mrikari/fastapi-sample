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


@router.get("", response_model=list[Todo])
async def get_todos():
    return await read_todo_list()


@router.post("", response_model=CreateTodoResult)
async def create_todo_item(body: CreateTodo = Body(..., title="Todo Data")):
    return await create_todo(body.title, is_complete=body.is_complete)


@router.get("/{id}")
async def get_todo_item(id: int = Path(..., title="ID")):
    return await read_todo(id)


@router.delete("/{id}")
async def delete_todo_item(id: int = Path(..., title="ID")):
    return await delete_todo(id)


@router.post("/{id}/complete")
async def change_complete_todo_item(id: int = Path(..., title="ID")):
    return await update_complete(id, True)


@router.post("/{id}/incomplete")
async def change_incomplete_todo_item(id: int = Path(..., title="ID")):
    return await update_complete(id, False)
