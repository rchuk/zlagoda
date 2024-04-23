from openapi_server.entities.product_entity import ProductEntity
from openapi_server.models.product import Product
from openapi_server.models.product_view import ProductView
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

from openapi_server.services.base.crud_service_base import CrudServiceBase
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase


class ProductService(CrudServiceBase[str, ProductEntity, ProductView, Product]):
    def __init__(
        self,
        repository: CrudRepositoryBase[str, ProductEntity],
        merger: MergerBase[ProductEntity, ProductView],
        validator: ValidatorBase[ProductEntity]
    ):
        super().__init__(
            repository, merger, validator,
            lambda: ProductEntity.model_construct(discount_id=None, has_discount=False),  # TODO
            self._build_dto
        )

    @staticmethod
    def _build_dto(entity: ProductEntity) -> Product:
        return Product(
            id=entity.id,
            archetype=entity.archetype,
            price=entity.price,
            quantity=entity.quantity,
            discount_id=entity.discount_id,
            has_discount=entity.has_discount,
        )
