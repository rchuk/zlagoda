from abc import ABC, abstractmethod
from typing import Generic, TypeVar

EntityT = TypeVar("EntityT")


class ValidatorBase(ABC, Generic[EntityT]):
    @abstractmethod
    def validate(self, entity: EntityT):
        ...
