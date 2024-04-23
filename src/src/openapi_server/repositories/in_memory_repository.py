from typing import TypeVar, List, Optional, Dict, Callable

from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

IdT = TypeVar("IdT")
EntityT = TypeVar("EntityT")


class InMemoryRepository(CrudRepositoryBase[IdT, EntityT]):
    def __init__(
        self,
        test_data: Optional[List[EntityT]] = None,
        id_getter: Optional[Callable[[EntityT], IdT]] = None,
        id_setter: Optional[Callable[[EntityT, IdT], None]] = None,
    ) -> None:
        self._id_getter = id_getter or (lambda entity: entity.id)
        self._id_setter = id_setter or (lambda entity, id: setattr(entity, "id", id))
        self._items: Dict[IdT, EntityT] = dict(map(lambda x: (self._id_getter(x), x), test_data))

        if len(self._items) == 0:
            self._counter = 0
        elif any(map(lambda id: isinstance(id, int), self._items.keys())):
            self._counter = max(self._items.keys()) + 1

    def create(self, entity: EntityT) -> IdT:
        id = self._id_getter(entity)
        copy = entity.copy(deep=True)
        if isinstance(id, int):
            self._id_setter(copy, self._counter)
            self._items[self._counter] = copy
            res = self._counter
            self._counter += 1

            return res

        else:
            self._items[id] = copy

            return id

    def get(self, id: IdT) -> EntityT:
        try:
            return self._items[id].copy(deep=True)
        except KeyError:
            return None

    def update(self, entity: EntityT) -> bool:
        self._items[self._id_getter(entity)] = entity.copy(deep=True)

        return True

    def delete(self, id: IdT) -> bool:
        return self._items.pop(id, None) is not None

    def list(self, criteria: Optional) -> List[EntityT]:
        # TODO: Filter
        return list(map(lambda item: item.copy(deep=True), self._items.values()))

    def count(self, criteria: Optional) -> int:
        # TODO: Filter
        return len(self._items)
