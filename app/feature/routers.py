from fastapi import APIRouter
from feature.root.router import router as root_router
from feature.todo.router import router as todo_router

api_router = APIRouter()

api_router.include_router(root_router, prefix="", tags=["Root"])
api_router.include_router(todo_router, prefix="/todos", tags=["Todo"])
