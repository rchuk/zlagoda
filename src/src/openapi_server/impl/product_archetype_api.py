from typing import Dict

from openapi_server.apis.product_archetype_api_base import BaseProductArchetypeApi

from openapi_server.models.product_archetype import ProductArchetype
from openapi_server.models.product_archetype_criteria import ProductArchetypeCriteria
from openapi_server.models.product_archetype_list_response import ProductArchetypeListResponse
from openapi_server.models.product_archetype_view import ProductArchetypeView


class ProductArchetypeApi(BaseProductArchetypeApi):
    def __init__(self):
        self._archetypes: Dict[int, ProductArchetype] = {
            0: ProductArchetype(
                id=0,
                name="Яблука",
                category=0,
                manufacturer="Зібрані десь",
                description="Дуже гарні червоні яблука"
            ),
            1: ProductArchetype(
                id=1,
                name="Печиво шоколадне",
                category=0,
                manufacturer="Roshen",
                description="Печиво з шоколадною крихтою"
            ),
            4: ProductArchetype(
                id=4,
                name="Мило",
                category=3,
                manufacturer="Невідомо хто",
                description="Просто мило"
            )
        }

    def create_product_archetype(
        self,
        product_archetype_view: ProductArchetypeView,
    ) -> int:
        raise NotImplementedError()


    def delete_product_archetype(
        self,
        id: int,
    ) -> bool:
        raise NotImplementedError()


    def get_product_archetype_by_id(
        self,
        id: int,
    ) -> ProductArchetype:
        return self._archetypes[id]


    def get_product_archetype_list(
        self,
        product_archetype_criteria: ProductArchetypeCriteria,
    ) -> ProductArchetypeListResponse:
        return ProductArchetypeListResponse(totalCount=len(self._archetypes), items=list(self._archetypes.values()))


    def update_product_archetype(
        self,
        id: int,
        product_archetype_view: ProductArchetypeView,
    ) -> bool:
        raise NotImplementedError()
