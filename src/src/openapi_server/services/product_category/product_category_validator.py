from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.models.product_category import ProductCategory
from openapi_server.services.base.validator_base import ValidatorBase, EntityT


class ProductCategoryValidator(ValidatorBase[ProductCategory]):
    def validate_create(self, entity: EntityT):
        self.validate_fields(entity)

    def validate_update(self, entity: EntityT):
        self.validate_fields(entity)

    def validate_fields(self, entity: ProductCategory):
        if len(entity.name.strip()) == 0:
            raise ValidationError("Назва категорії продукту не може бути порожньою")
