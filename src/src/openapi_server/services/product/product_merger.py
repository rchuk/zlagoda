from openapi_server.entities.product_entity import ProductEntity
from openapi_server.models.product_view import ProductView
from openapi_server.services.base.merger_base import MergerBase


class ProductMerger(MergerBase[ProductEntity, ProductView]):
    def merge_create(self, entity: ProductEntity, view: ProductView):
        self._merge_main_fields(entity, view)

    def merge_edit(self, entity: ProductEntity, view: ProductView):
        self._merge_main_fields(entity, view)

    def _merge_main_fields(self, entity: ProductEntity, view: ProductView):
        entity.id = view.id
        entity.archetype = view.archetype
        entity.price = view.price
        entity.quantity = view.quantity
