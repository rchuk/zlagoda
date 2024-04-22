from openapi_server.entities.product_archetype_entity import ProductArchetypeEntity
from openapi_server.entities.product_entity import ProductEntity
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase
from openapi_server.services.base.validator_base import ValidatorBase


class ProductValidator(ValidatorBase[ProductEntity]):
    def __init__(
        self,
        product_repository: CrudRepositoryBase[str, ProductEntity],
        product_archetype_repository: CrudRepositoryBase[int, ProductArchetypeEntity],
    ):
        self._product_repository = product_repository
        self._product_archetype_repository = product_archetype_repository

    def validate_create(self, entity: ProductEntity):
        if self._product_repository.get(entity.id):
            raise ValidationError("Продукт з даним UPC кодом вже існує")

        self.validate_fields(entity)

    def validate_update(self, entity: ProductEntity, id: str):
        if entity.id != id and self._product_repository.get(id):
            raise ValidationError("Продукт з даним UPC кодом вже існує")

        self.validate_fields(entity)

    def validate_fields(self, entity: ProductEntity):
        if len(entity.id) != 12:
            raise ValidationError("Невірний UPC код")
        if self._product_archetype_repository.get(entity.archetype) is None:
            raise ValidationError("Типу продукуту не існує")
        if entity.price < 0:
            raise ValidationError("Ціна не може бути від'ємною")
        if entity.quantity < 0:
            raise ValidationError("Кількість не може бути від'ємною")
