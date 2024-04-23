from abc import ABC
from typing import Generic, TypeVar

EntityT = TypeVar("EntityT")


class ValidatorBase(ABC, Generic[EntityT]):
    def validate_create(self, entity: EntityT):
        pass

    def validate_view(self, entity: EntityT):
        pass

    def validate_update(self, entity: EntityT, id):
        pass

    def validate_delete(self, entity: EntityT):
        pass