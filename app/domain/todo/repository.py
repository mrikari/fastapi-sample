from typing import Generic
from uuid import UUID

from core.repository import AnySession, RepositoryMutateBase, RepositoryQueryBase
from domain.todo.model import Todo


class TodoRepository(
    RepositoryQueryBase[Todo, UUID],
    RepositoryMutateBase[Todo, UUID],
    Generic[AnySession],
):
    def __init__(self, session: AnySession) -> None:
        """非同期DBセッション

        Args:
            session (AsyncSession): _description_
        """
        self.session = session
