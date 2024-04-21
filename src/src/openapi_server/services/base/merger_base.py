from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

EntityT = TypeVar("EntityT")
ViewT = TypeVar("ViewT")


class MergerBase(ABC, Generic[EntityT, ViewT]):
    @abstractmethod
    def merge_create(self, entity: EntityT, view: ViewT):
        ...

    @abstractmethod
    def merge_edit(self, entity: EntityT, view: ViewT):
        ...

    @staticmethod
    def _strip_optional(value: Optional[str]):
        if value is None:
            return None

        return value.strip() or None
