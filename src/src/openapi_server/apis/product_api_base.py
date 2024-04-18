# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.product import Product
from openapi_server.models.product_criteria import ProductCriteria
from openapi_server.models.product_list_response import ProductListResponse
from openapi_server.models.product_view import ProductView


class BaseProductApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProductApi.subclasses = BaseProductApi.subclasses + (cls,)
    def create_product(
        self,
        product_view: ProductView,
    ) -> int:
        """Create a new product"""
        ...


    def delete_product(
        self,
        id: int,
    ) -> bool:
        """Delete a product by id"""
        ...


    def get_product_by_id(
        self,
        id: int,
    ) -> Product:
        """Get product by id"""
        ...


    def get_product_list(
        self,
        product_criteria: ProductCriteria,
    ) -> ProductListResponse:
        """Get list of products"""
        ...


    def update_prodact(
        self,
        id: int,
        product_view: ProductView,
    ) -> bool:
        """Update existing product"""
        ...
