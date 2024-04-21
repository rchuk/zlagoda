from dependency_injector.wiring import Provide, inject

from openapi_server.apis.product_api_base import BaseProductApi
from openapi_server.containers import ApplicationContainer

from openapi_server.models.product import Product
from openapi_server.models.product_criteria import ProductCriteria
from openapi_server.models.product_list_response import ProductListResponse
from openapi_server.models.product_view import ProductView
from openapi_server.services.product.product_service import ProductService


class ProductApi(BaseProductApi):
    @inject
    def __init__(
        self,
        product_service: ProductService = Provide[ApplicationContainer.services.product_service]
    ):
        self._service = product_service

    def create_product(
        self,
        product_view: ProductView,
    ) -> str:
        return self._service.create(product_view)

    def delete_product(
        self,
        id: str,
    ) -> bool:
        return self._service.delete(id)

    def get_product_by_id(
        self,
        id: str,
    ) -> Product:
        return self._service.get(id)

    def get_product_list(
        self,
        product_criteria: ProductCriteria,
    ) -> ProductListResponse:
        return ProductListResponse(
            totalCount=self._service.count(product_criteria),
            items=self._service.list(product_criteria),
        )

    def update_prodact(
        self,
        id: str,
        product_view: ProductView,
    ) -> bool:
        return self._service.update(id, product_view)
