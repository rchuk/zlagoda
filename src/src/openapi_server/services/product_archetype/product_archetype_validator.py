from openapi_server.entities.product_archetype_entity import ProductArchetypeEntity
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase
from openapi_server.services.base.validator_base import ValidatorBase


class ProductArchetypeValidator(ValidatorBase[ProductArchetypeEntity]):
    def __init__(self, product_category_repository: CrudRepositoryBase[int, ProductArchetypeEntity]):
        self._product_category_repository = product_category_repository

    def validate_create(self, entity: ProductArchetypeEntity):
        self.validate_fields(entity)

    def validate_update(self, entity: ProductArchetypeEntity):
        self.validate_fields(entity)

    def validate_fields(self, entity: ProductArchetypeEntity):
        if len(entity.name) == 0:
            raise ValidationError("Назва типу продукту не може бути порожньою")
        if self._product_category_repository.get(entity.category) is None:
            raise ValidationError("Категорії продукту не існує")
        if len(entity.manufacturer) == 0:
            raise ValidationError("Виробник продукту не може бути порожнім")
        if len(entity.description) == 0:
            raise ValidationError("Опис продукту не може бути порожнім")
