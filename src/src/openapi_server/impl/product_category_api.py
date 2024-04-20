from typing import Dict

from openapi_server.apis.product_category_api_base import BaseProductCategoryApi

from openapi_server.models.product_category import ProductCategory
from openapi_server.models.product_category_criteria import ProductCategoryCriteria
from openapi_server.models.product_category_list_response import ProductCategoryListResponse
from openapi_server.models.product_category_view import ProductCategoryView


class ProductCategoryApi(BaseProductCategoryApi):
    def __init__(self):
        self._categories: Dict[int, ProductCategory] = {
            0: ProductCategory(
                id=0,
                name="Харчові продукти"
            ),
            1: ProductCategory(
                id=3,
                name="Косметика та парфумерія"
            )
        }

    def create_product_category(
        self,
        product_category_view: ProductCategoryView,
    ) -> int:
        raise NotImplementedError()


    def delete_product_category(
        self,
        id: int,
    ) -> bool:
        raise NotImplementedError()


    def get_product_category_by_id(
        self,
        id: int,
    ) -> ProductCategory:
        return self._categories[id]


    def get_product_category_list(
        self,
        product_category_criteria: ProductCategoryCriteria,
    ) -> ProductCategoryListResponse:
        return ProductCategoryListResponse(totalCount=len(self._categories), items=list(self._categories.values()))


    def update_product_category(
        self,
        id: int,
        product_category_view: ProductCategoryView,
    ) -> bool:
        raise NotImplementedError()
