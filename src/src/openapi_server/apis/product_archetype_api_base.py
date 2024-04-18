# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.product_archetype import ProductArchetype
from openapi_server.models.product_archetype_criteria import ProductArchetypeCriteria
from openapi_server.models.product_archetype_list_response import ProductArchetypeListResponse
from openapi_server.models.product_archetype_view import ProductArchetypeView


class BaseProductArchetypeApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProductArchetypeApi.subclasses = BaseProductArchetypeApi.subclasses + (cls,)
    def create_product_archetype(
        self,
        product_archetype_view: ProductArchetypeView,
    ) -> int:
        """Create a new product archetype"""
        ...


    def delete_product_archetype(
        self,
        id: int,
    ) -> bool:
        """Delete a product archetype by id"""
        ...


    def get_product_archetype_by_id(
        self,
        id: int,
    ) -> ProductArchetype:
        """Get product archetype by id"""
        ...


    def get_product_archetype_list(
        self,
        product_archetype_criteria: ProductArchetypeCriteria,
    ) -> ProductArchetypeListResponse:
        """Get list of product archetypes"""
        ...


    def update_product_archetype(
        self,
        id: int,
        product_archetype_view: ProductArchetypeView,
    ) -> bool:
        """Update existing product archetype"""
        ...
