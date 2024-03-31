from abc import ABC, abstractclassmethod
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
IDType = TypeVar("IDType")
AnySession = TypeVar("AnySession")


class RepositoryMutateBase(ABC, Generic[ModelType, IDType]):
    @abstractclassmethod
    async def create(self, entity: ModelType): ...

    @abstractclassmethod
    async def update(self, id: IDType, entity: ModelType): ...

    @abstractclassmethod
    async def delete(self, id: UUID): ...


class RepositoryQueryBase(ABC, Generic[ModelType, IDType]):
    @abstractclassmethod
    async def find_all(self) -> list[ModelType]: ...

    @abstractclassmethod
    async def find_by_id(self, id: IDType) -> list[ModelType]: ...
