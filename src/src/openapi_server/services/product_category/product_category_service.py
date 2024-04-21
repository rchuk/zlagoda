from openapi_server.entities.product_category_entity import ProductCategoryEntity
from openapi_server.models.product_category import ProductCategory
from openapi_server.models.product_category_view import ProductCategoryView
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

from openapi_server.services.base.crud_service_base import CrudServiceBase
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase


class ProductCategoryService(CrudServiceBase[int, ProductCategoryEntity, ProductCategoryView, ProductCategory]):
    def __init__(
        self,
        repository: CrudRepositoryBase[id, ProductCategoryEntity],
        merger: MergerBase[ProductCategoryEntity, ProductCategoryView],
        validator: ValidatorBase[ProductCategoryEntity]
    ):
        super().__init__(
            repository, merger, validator,
            lambda: ProductCategoryEntity.model_construct(id=-1),
            self._build_dto
        )

    @staticmethod
    def _build_dto(entity: ProductCategoryEntity) -> ProductCategory:
        return ProductCategory(id=entity.id, name=entity.name)
