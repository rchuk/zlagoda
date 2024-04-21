from typing import Dict

from openapi_server.apis.product_api_base import BaseProductApi

from openapi_server.models.product import Product
from openapi_server.models.product_criteria import ProductCriteria
from openapi_server.models.product_list_response import ProductListResponse
from openapi_server.models.product_view import ProductView


class ProductApi(BaseProductApi):
    def __init__(self):
        self._products: Dict[str, Product] = {
            "000000000001": Product(
                id="000000000001",
                archetype=0,
                price=100,
                quantity=50,
                has_discount=False
            ),
            "000000000002": Product(
                id="000000000002",
                archetype=0,
                price=80,
                quantity=20,
                has_discount=True
            ),
            "000000000013": Product(
                id="000000000013",
                archetype=1,
                price=150,
                quantity=330,
                has_discount=False
            ),
            "000000242401": Product(
                id="000000242401",
                archetype=2,
                price=666,
                quantity=228,
                has_discount=False
            )
        }

    def create_product(
        self,
        product_view: ProductView,
    ) -> int:
        raise NotImplementedError()


    def delete_product(
        self,
        id: int,
    ) -> bool:
        raise NotImplementedError()


    def get_product_by_id(
        self,
        id: int,
    ) -> Product:
        return self._products.get(id)


    def get_product_list(
        self,
        product_criteria: ProductCriteria,
    ) -> ProductListResponse:
        return ProductListResponse(totalCount=len(self._products), items=list(self._products.values()))


    def update_prodact(
        self,
        id: int,
        product_view: ProductView,
    ) -> bool:
        raise NotImplementedError()
