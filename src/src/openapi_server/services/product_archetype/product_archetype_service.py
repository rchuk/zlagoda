from openapi_server.entities.product_archetype_entity import ProductArchetypeEntity
from openapi_server.models.product_archetype import ProductArchetype
from openapi_server.models.product_archetype_view import ProductArchetypeView
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

from openapi_server.services.base.crud_service_base import CrudServiceBase
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase


class ProductArchetypeService(CrudServiceBase[int, ProductArchetypeEntity, ProductArchetypeView, ProductArchetype]):
    def __init__(
        self,
        repository: CrudRepositoryBase[id, ProductArchetypeEntity],
        merger: MergerBase[ProductArchetypeEntity, ProductArchetypeView],
        validator: ValidatorBase[ProductArchetypeEntity]
    ):
        super().__init__(
            repository, merger, validator,
            lambda: ProductArchetypeEntity.model_construct(id=-1),
            self._build_dto
        )

    @staticmethod
    def _build_dto(entity: ProductArchetypeEntity) -> ProductArchetype:
        return ProductArchetype(
            id=entity.id,
            name=entity.name,
            category=entity.category,
            manufacturer=entity.manufacturer,
            description=entity.description
        )
