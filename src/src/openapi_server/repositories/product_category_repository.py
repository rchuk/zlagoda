from typing import Optional, List, Dict

from openapi_server.entities.product_category_entity import ProductCategoryEntity
from openapi_server.models.product_category_criteria import ProductCategoryCriteria

from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase


class ProductCategoryRepository(CrudRepositoryBase[int, ProductCategoryEntity]):
    def __init__(self):
        self._counter: int = 4
        self._items: Dict[int, ProductCategoryEntity] = {
            0: ProductCategoryEntity(
                id=0,
                name="Харчові продукти"
            ),
            3: ProductCategoryEntity(
                id=3,
                name="Косметика та парфумерія"
            )
        }

    def create(self, entity: ProductCategoryEntity) -> int:
        entity.id = self._counter
        self._items[self._counter] = entity.copy(deep=True)
        self._counter += 1

        return entity.id

    def update(self, entity: ProductCategoryEntity) -> bool:
        self._items[entity.id] = entity.copy(deep=True)

        return True

    def get(self, id: int) -> ProductCategoryEntity:
        return self._items[id].copy(deep=True)

    def delete(self, id: int) -> bool:
        return self._items.pop(id, None) is not None

    def list(self, criteria: Optional[ProductCategoryCriteria] = None) -> List[ProductCategoryEntity]:
        # TODO: Filter
        return list(map(lambda item: item.copy(deep=True), self._items.values()))

    def count(self, criteria: Optional[ProductCategoryCriteria] = None) -> int:
        # TODO: Filter
        return len(self._items)
