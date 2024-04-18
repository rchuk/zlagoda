# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.product_category_api_base import BaseProductCategoryApi
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
from openapi_server.models.product_category import ProductCategory
from openapi_server.models.product_category_criteria import ProductCategoryCriteria
from openapi_server.models.product_category_list_response import ProductCategoryListResponse
from openapi_server.models.product_category_view import ProductCategoryView


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.put(
    "/api/product-category/",
    responses={
        200: {"model": int, "description": "Id of new product category"},
    },
    tags=["product-category"],
    summary="Create a new product category",
    response_model_by_alias=True,
)
async def create_product_category(
    product_category_view: ProductCategoryView = Body(None, description=""),
) -> int:
    """Create a new product category"""
    return BaseProductCategoryApi.subclasses[0]().create_product_category(product_category_view)


@router.delete(
    "/api/product-category/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether productCategory was deleted"},
    },
    tags=["product-category"],
    summary="Delete a product category by id",
    response_model_by_alias=True,
)
async def delete_product_category(
    id: int = Path(..., description=""),
) -> bool:
    """Delete a product category by id"""
    return BaseProductCategoryApi.subclasses[0]().delete_product_category(id)


@router.get(
    "/api/product-category/{id}",
    responses={
        200: {"model": ProductCategory, "description": "Product category by id"},
    },
    tags=["product-category"],
    summary="Get product category by id",
    response_model_by_alias=True,
)
async def get_product_category_by_id(
    id: int = Path(..., description=""),
) -> ProductCategory:
    """Get product category by id"""
    return BaseProductCategoryApi.subclasses[0]().get_product_category_by_id(id)


@router.get(
    "/api/product-category/",
    responses={
        200: {"model": ProductCategoryListResponse, "description": "List of product categories"},
    },
    tags=["product-category"],
    summary="Get list of product categories",
    response_model_by_alias=True,
)
async def get_product_category_list(
    product_category_criteria: ProductCategoryCriteria = Body(None, description=""),
) -> ProductCategoryListResponse:
    """Get list of product categories"""
    return BaseProductCategoryApi.subclasses[0]().get_product_category_list(product_category_criteria)


@router.post(
    "/api/product-category/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether product category was updated"},
    },
    tags=["product-category"],
    summary="Update existing product category",
    response_model_by_alias=True,
)
async def update_product_category(
    id: int = Path(..., description=""),
    product_category_view: ProductCategoryView = Body(None, description=""),
) -> bool:
    """Update existing product category"""
    return BaseProductCategoryApi.subclasses[0]().update_product_category(id, product_category_view)
