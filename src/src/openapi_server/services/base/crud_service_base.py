from typing import TypeVar, Generic, List, Callable, Optional
from abc import ABC

from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase


IdT = TypeVar("IdT")
EntityT = TypeVar("EntityT")
ViewT = TypeVar("ViewT")
DtoT = TypeVar("DtoT")


class CrudServiceBase(ABC, Generic[IdT, EntityT, ViewT, DtoT]):
    def __init__(
        self,
        repository: CrudRepositoryBase[IdT, EntityT],
        merger: MergerBase[EntityT, ViewT],
        validator: ValidatorBase[EntityT],
        entity_factory: Callable[[], EntityT],
        converter: Callable[[EntityT], DtoT]
    ):
        self._repository = repository
        self._merger = merger
        self._validator = validator
        self._entity_factory = entity_factory
        self._converter = converter

    def create(self, view: ViewT) -> IdT:
        entity = self._entity_factory()
        self._merger.merge_create(entity, view)
        self._validator.validate(entity)

        return self._repository.create(entity)

    def get(self, id: IdT) -> DtoT:
        return self._converter(self.get_entity(id))

    def update(self, id: IdT, view: ViewT) -> bool:
        entity = self._repository.get(id)
        self._merger.merge_edit(entity, view)
        self._validator.validate(entity)

        return self._repository.update(entity)

    def delete(self, id: IdT) -> bool:
        return self._repository.delete(id)

    def list(self, criteria: Optional) -> List[DtoT]:
        return list(map(self._converter, self.list_entity(criteria)))

    def count(self, criteria) -> int:
        return self._repository.count(criteria)

    def get_entity(self, id: IdT) -> EntityT:
        return self._repository.get(id)

    def list_entity(self, criteria: Optional) -> List[EntityT]:
        return self._repository.list(criteria)
