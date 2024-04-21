from abc import ABC, abstractmethod
from typing import Generic, TypeVar

EntityT = TypeVar("EntityT")
ViewT = TypeVar("ViewT")


class MergerBase(ABC, Generic[EntityT, ViewT]):
    @abstractmethod
    def merge_create(self, entity: EntityT, view: ViewT):
        ...

    @abstractmethod
    def merge_edit(self, entity: EntityT, view: ViewT):
        ...
