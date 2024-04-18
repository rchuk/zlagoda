# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.product_api_base import BaseProductApi
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
from openapi_server.models.product import Product
from openapi_server.models.product_criteria import ProductCriteria
from openapi_server.models.product_list_response import ProductListResponse
from openapi_server.models.product_view import ProductView


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.put(
    "/api/product",
    responses={
        200: {"model": int, "description": "Id of new product"},
    },
    tags=["product"],
    summary="Create a new product",
    response_model_by_alias=True,
)
async def create_product(
    product_view: ProductView = Body(None, description=""),
) -> int:
    """Create a new product"""
    return BaseProductApi.subclasses[0]().create_product(product_view)


@router.delete(
    "/api/product/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether product was deleted"},
    },
    tags=["product"],
    summary="Delete a product by id",
    response_model_by_alias=True,
)
async def delete_product(
    id: int = Path(..., description=""),
) -> bool:
    """Delete a product by id"""
    return BaseProductApi.subclasses[0]().delete_product(id)


@router.get(
    "/api/product/{id}",
    responses={
        200: {"model": Product, "description": "product by id"},
    },
    tags=["product"],
    summary="Get product by id",
    response_model_by_alias=True,
)
async def get_product_by_id(
    id: int = Path(..., description=""),
) -> Product:
    """Get product by id"""
    return BaseProductApi.subclasses[0]().get_product_by_id(id)


@router.get(
    "/api/product",
    responses={
        200: {"model": ProductListResponse, "description": "List of products"},
    },
    tags=["product"],
    summary="Get list of products",
    response_model_by_alias=True,
)
async def get_product_list(
    product_criteria: ProductCriteria = Body(None, description=""),
) -> ProductListResponse:
    """Get list of products"""
    return BaseProductApi.subclasses[0]().get_product_list(product_criteria)


@router.post(
    "/api/product/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether product was updated"},
    },
    tags=["product"],
    summary="Update existing product",
    response_model_by_alias=True,
)
async def update_prodact(
    id: int = Path(..., description=""),
    product_view: ProductView = Body(None, description=""),
) -> bool:
    """Update existing product"""
    return BaseProductApi.subclasses[0]().update_prodact(id, product_view)
