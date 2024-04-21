from typing import TypeVar, List, Optional, Dict

from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

IdT = TypeVar("IdT")
EntityT = TypeVar("EntityT")


class InMemoryRepository(CrudRepositoryBase[IdT, EntityT]):
    def __init__(self, test_data: Optional[List[EntityT]] = None):
        self._items: Dict[IdT, EntityT] = dict(map(lambda x: (x.id, x), test_data))
        self._counter = max(self._items.keys()) + 1

    def create(self, entity: EntityT) -> IdT:
        entity.id = self._counter
        self._items[self._counter] = entity.copy(deep=True)
        self._counter += 1

        return entity.id

    def get(self, id: IdT) -> EntityT:
        return self._items[id].copy(deep=True)

    def update(self, entity: EntityT) -> bool:
        self._items[entity.id] = entity.copy(deep=True)

        return True

    def delete(self, id: IdT) -> bool:
        return self._items.pop(id, None) is not None

    def list(self, criteria: Optional) -> List[EntityT]:
        # TODO: Filter
        return list(map(lambda item: item.copy(deep=True), self._items.values()))

    def count(self, criteria: Optional) -> int:
        # TODO: Filter
        return len(self._items)
