from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

IdT = TypeVar("IdT")
EntityT = TypeVar("EntityT")


class CrudRepositoryBase(ABC, Generic[IdT, EntityT]):
    @abstractmethod
    def create(self, entity: EntityT) -> IdT:
        ...

    @abstractmethod
    def get(self, id: IdT) -> EntityT:
        ...

    @abstractmethod
    def update(self, entity: EntityT) -> bool:
        ...

    @abstractmethod
    def delete(self, id: IdT) -> bool:
        ...

    @abstractmethod
    def list(self, criteria: Optional) -> List[EntityT]:
        ...

    @abstractmethod
    def count(self, criteria: Optional) -> int:
        ...
