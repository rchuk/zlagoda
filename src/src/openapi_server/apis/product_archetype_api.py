# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.product_archetype_api_base import BaseProductArchetypeApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.product_archetype import ProductArchetype
from openapi_server.models.product_archetype_criteria import ProductArchetypeCriteria
from openapi_server.models.product_archetype_list_response import ProductArchetypeListResponse
from openapi_server.models.product_archetype_view import ProductArchetypeView


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.put(
    "/api/product-archetype",
    responses={
        200: {"model": int, "description": "Id of new product archetype"},
    },
    tags=["product-archetype"],
    summary="Create a new product archetype",
    response_model_by_alias=True,
)
async def create_product_archetype(
    product_archetype_view: ProductArchetypeView = Body(None, description=""),
) -> int:
    """Create a new product archetype"""
    return BaseProductArchetypeApi.subclasses[0]().create_product_archetype(product_archetype_view)


@router.delete(
    "/api/product-archetype/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether product archetype was deleted"},
    },
    tags=["product-archetype"],
    summary="Delete a product archetype by id",
    response_model_by_alias=True,
)
async def delete_product_archetype(
    id: int = Path(..., description=""),
) -> bool:
    """Delete a product archetype by id"""
    return BaseProductArchetypeApi.subclasses[0]().delete_product_archetype(id)


@router.get(
    "/api/product-archetype/{id}",
    responses={
        200: {"model": ProductArchetype, "description": "Product archetype by id"},
    },
    tags=["product-archetype"],
    summary="Get product archetype by id",
    response_model_by_alias=True,
)
async def get_product_archetype_by_id(
    id: int = Path(..., description=""),
) -> ProductArchetype:
    """Get product archetype by id"""
    return BaseProductArchetypeApi.subclasses[0]().get_product_archetype_by_id(id)


@router.post(
    "/api/product-archetype",
    responses={
        200: {"model": ProductArchetypeListResponse, "description": "List of product archetypes"},
    },
    tags=["product-archetype"],
    summary="Get list of product archetypes",
    response_model_by_alias=True,
)
async def get_product_archetype_list(
    product_archetype_criteria: ProductArchetypeCriteria = Body(None, description=""),
) -> ProductArchetypeListResponse:
    """Get list of product archetypes"""
    return BaseProductArchetypeApi.subclasses[0]().get_product_archetype_list(product_archetype_criteria)


@router.post(
    "/api/product-archetype/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether product archetype was updated"},
    },
    tags=["product-archetype"],
    summary="Update existing product archetype",
    response_model_by_alias=True,
)
async def update_product_archetype(
    id: int = Path(..., description=""),
    product_archetype_view: ProductArchetypeView = Body(None, description=""),
) -> bool:
    """Update existing product archetype"""
    return BaseProductArchetypeApi.subclasses[0]().update_product_archetype(id, product_archetype_view)
