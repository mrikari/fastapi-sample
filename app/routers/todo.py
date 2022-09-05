from fastapi import APIRouter, Path

from database import database
from models.todo import CreateTodo
from schemas.todo import todos

router = APIRouter(prefix="/todos", tags=["Todo"])


@router.get("")
async def get_todo_list():
    query = todos.select()
    return await database.fetch_all(query)


@router.post("")
async def create_todo(body: CreateTodo):
    query = todos.insert().values(
        title=body.title, is_complete=body.is_complete
    )
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@router.get("/{id}")
async def get_todo_item(id: int = Path(..., title="ID")):
    query = todos.select(todos.c.id == id)
    item = await database.fetch_one(query)
    return item


@router.delete("/{id}")
async def delete_todo_item(id: int = Path(..., title="ID")):
    query = todos.select(todos.c.id == id)
    item = await database.fetch_one(query)
    if not item:
        return {"result": False}
    query = todos.delete().where(todos.c.id == id)
    result = await database.execute(query)
    return {"result": result}


@router.post("/{id}/complete")
async def change_complete_todo_item(id: int = Path(..., title="ID")):
    query = todos.select(todos.c.id == id)
    item = await database.fetch_one(query)
    if not item:
        return {"result": False}
    query = todos.update().where(todos.c.id == id).values(is_complete=True)
    result = await database.execute(query)
    return {"result": result}


@router.post("/{id}/incomplete")
async def change_incomplete_todo_item(id: int = Path(..., title="ID")):
    query = todos.select(todos.c.id == id)
    item = await database.fetch_one(query)
    if not item:
        return {"result": False}
    query = todos.update().where(todos.c.id == id).values(is_complete=False)
    result = await database.execute(query)
    return {"result": result}
