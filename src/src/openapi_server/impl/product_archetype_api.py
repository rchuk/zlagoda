from dependency_injector.wiring import Provide, inject

from openapi_server.apis.product_archetype_api_base import BaseProductArchetypeApi
from openapi_server.containers import ApplicationContainer

from openapi_server.models.product_archetype import ProductArchetype
from openapi_server.models.product_archetype_criteria import ProductArchetypeCriteria
from openapi_server.models.product_archetype_list_response import ProductArchetypeListResponse
from openapi_server.models.product_archetype_view import ProductArchetypeView

from openapi_server.services.product_archetype.product_archetype_service import ProductArchetypeService


class ProductArchetypeApi(BaseProductArchetypeApi):
    @inject
    def __init__(
        self,
        product_archetype_service: ProductArchetypeService = Provide[ApplicationContainer.services.product_archetype_service]
    ):
        self._service = product_archetype_service

    def create_product_archetype(
        self,
        product_archetype_view: ProductArchetypeView,
    ) -> int:
        return self._service.create(product_archetype_view)

    def delete_product_archetype(
        self,
        id: int,
    ) -> bool:
        return self._service.delete(id)

    def get_product_archetype_by_id(
        self,
        id: int,
    ) -> ProductArchetype:
        return self._service.get(id)

    def get_product_archetype_list(
        self,
        product_archetype_criteria: ProductArchetypeCriteria,
    ) -> ProductArchetypeListResponse:
        return ProductArchetypeListResponse(
            totalCount=self._service.count(product_archetype_criteria),
            items=self._service.list(product_archetype_criteria)
        )

    def update_product_archetype(
        self,
        id: int,
        product_archetype_view: ProductArchetypeView,
    ) -> bool:
        return self._service.update(id, product_archetype_view)
