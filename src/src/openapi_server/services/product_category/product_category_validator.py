from openapi_server.entities.product_category_entity import ProductCategoryEntity
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.services.base.validator_base import ValidatorBase


class ProductCategoryValidator(ValidatorBase[ProductCategoryEntity]):
    def validate_create(self, entity: ProductCategoryEntity):
        self.validate_fields(entity)

    def validate_update(self, entity: ProductCategoryEntity, id):
        self.validate_fields(entity)

    def validate_fields(self, entity: ProductCategoryEntity):
        if len(entity.name) == 0:
            raise ValidationError("Назва категорії продукту не може бути порожньою")
