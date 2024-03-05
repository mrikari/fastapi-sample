from fastapi import APIRouter
from routers import root, todo

api_router = APIRouter()

api_router.include_router(root.router, prefix="", tags=["Root"])
api_router.include_router(todo.router, prefix="/todos", tags=["Todo"])
