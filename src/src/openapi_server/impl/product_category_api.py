from openapi_server.apis.product_category_api_base import BaseProductCategoryApi
from openapi_server.containers import ApplicationContainer

from openapi_server.models.product_category import ProductCategory
from openapi_server.models.product_category_criteria import ProductCategoryCriteria
from openapi_server.models.product_category_list_response import ProductCategoryListResponse
from openapi_server.models.product_category_view import ProductCategoryView

from dependency_injector.wiring import Provide, inject

from openapi_server.services.product_category.product_category_service import ProductCategoryService


class ProductCategoryApi(BaseProductCategoryApi):
    @inject
    def __init__(
        self,
        product_category_service: ProductCategoryService = Provide[ApplicationContainer.services.product_category_service]
    ):
        self._service = product_category_service

    def create_product_category(
        self,
        product_category_view: ProductCategoryView,
    ) -> int:
        return self._service.create(product_category_view)

    def delete_product_category(
        self,
        id: int,
    ) -> bool:
        return self._service.delete(id)

    def get_product_category_by_id(
        self,
        id: int,
    ) -> ProductCategory:
        return self._service.get(id)

    def get_product_category_list(
        self,
        product_category_criteria: ProductCategoryCriteria,
    ) -> ProductCategoryListResponse:
        return ProductCategoryListResponse(
            total_count=self._service.count(product_category_criteria),
            items=self._service.list(product_category_criteria)
        )

    def update_product_category(
        self,
        id: int,
        product_category_view: ProductCategoryView,
    ) -> bool:
        return self._service.update(id, product_category_view)
