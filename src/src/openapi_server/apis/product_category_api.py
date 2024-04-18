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
from openapi_server.models.product_category_view import ProductCategoryView


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/product-category/count",
    responses={
        200: {"model": int, "description": "Number of product categories"},
    },
    tags=["product-category"],
    summary="Count product categories",
    response_model_by_alias=True,
)
async def count_product_category(
) -> int:
    ...


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
    ...


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
    ...


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
    ...


@router.get(
    "/api/product-category/",
    responses={
        200: {"model": List[ProductCategory], "description": "List of product categories"},
    },
    tags=["product-category"],
    summary="Get list of product categories",
    response_model_by_alias=True,
)
async def get_product_category_list(
    product_category_criteria: ProductCategoryCriteria = Body(None, description=""),
) -> List[ProductCategory]:
    ...


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
    ...
