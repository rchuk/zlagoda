from openapi_server.entities.product_archetype_entity import ProductArchetypeEntity
from openapi_server.models.product_archetype_view import ProductArchetypeView
from openapi_server.services.base.merger_base import MergerBase


class ProductArchetypeMerger(MergerBase[ProductArchetypeEntity, ProductArchetypeView]):
    def merge_create(self, entity: ProductArchetypeEntity, view: ProductArchetypeView):
        self._merge_main_fields(entity, view)

    def merge_edit(self, entity: ProductArchetypeEntity, view: ProductArchetypeView):
        self._merge_main_fields(entity, view)

    def _merge_main_fields(self, entity: ProductArchetypeEntity, view: ProductArchetypeView):
        entity.name = view.name.strip()
        entity.category = view.category
        entity.manufacturer = view.manufacturer.strip()
        entity.description = view.description.strip()
