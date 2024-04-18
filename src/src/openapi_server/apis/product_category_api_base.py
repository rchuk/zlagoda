# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.product_category import ProductCategory
from openapi_server.models.product_category_criteria import ProductCategoryCriteria
from openapi_server.models.product_category_list_response import ProductCategoryListResponse
from openapi_server.models.product_category_view import ProductCategoryView


class BaseProductCategoryApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProductCategoryApi.subclasses = BaseProductCategoryApi.subclasses + (cls,)
    def create_product_category(
        self,
        product_category_view: ProductCategoryView,
    ) -> int:
        """Create a new product category"""
        ...


    def delete_product_category(
        self,
        id: int,
    ) -> bool:
        """Delete a product category by id"""
        ...


    def get_product_category_by_id(
        self,
        id: int,
    ) -> ProductCategory:
        """Get product category by id"""
        ...


    def get_product_category_list(
        self,
        product_category_criteria: ProductCategoryCriteria,
    ) -> ProductCategoryListResponse:
        """Get list of product categories"""
        ...


    def update_product_category(
        self,
        id: int,
        product_category_view: ProductCategoryView,
    ) -> bool:
        """Update existing product category"""
        ...
