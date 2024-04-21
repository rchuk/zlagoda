from openapi_server.entities.product_category_entity import ProductCategoryEntity
from openapi_server.models.product_category_view import ProductCategoryView
from openapi_server.services.base.merger_base import MergerBase


class ProductCategoryMerger(MergerBase[ProductCategoryEntity, ProductCategoryView]):
    def merge_create(self, entity: ProductCategoryEntity, view: ProductCategoryView):
        self.merge_main_fields(entity, view)

    def merge_edit(self, entity: ProductCategoryEntity, view: ProductCategoryView):
        self.merge_main_fields(entity, view)

    def merge_main_fields(self, entity: ProductCategoryEntity, view: ProductCategoryView):
        entity.name = view.name
