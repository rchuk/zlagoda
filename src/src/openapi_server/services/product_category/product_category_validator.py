from openapi_server.models.product_category import ProductCategory
from openapi_server.services.base.validator_base import ValidatorBase, EntityT


class ProductCategoryValidator(ValidatorBase[ProductCategory]):
    def validate(self, entity: ProductCategory):
        # TODO: Create exception class
        # if len(entity.name.strip()) == 0:
        #     raise
        pass
