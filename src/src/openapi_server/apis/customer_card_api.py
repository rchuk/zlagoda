# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.customer_card_api_base import BaseCustomerCardApi
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
from openapi_server.models.customer_card import CustomerCard
from openapi_server.models.customer_card_criteria import CustomerCardCriteria
from openapi_server.models.customer_card_view import CustomerCardView


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.put(
    "/api/customer-card",
    responses={
        200: {"model": int, "description": "Id of new customer card"},
    },
    tags=["customer-card"],
    summary="Create a new customer card",
    response_model_by_alias=True,
)
async def create_customer_card(
    customer_card_view: CustomerCardView = Body(None, description=""),
) -> int:
    ...


@router.delete(
    "/api/customer-card/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether customer card was deleted"},
    },
    tags=["customer-card"],
    summary="Delete a customer card by id",
    response_model_by_alias=True,
)
async def delete_customer_card(
    id: int = Path(..., description=""),
) -> bool:
    ...


@router.get(
    "/api/customer-card/{id}",
    responses={
        200: {"model": CustomerCard, "description": "Customer card by id"},
    },
    tags=["customer-card"],
    summary="Get customer card by id",
    response_model_by_alias=True,
)
async def get_customer_card_by_id(
    id: int = Path(..., description=""),
) -> CustomerCard:
    ...


@router.get(
    "/api/customer-card",
    responses={
        200: {"model": CustomerCard, "description": "List of customer cards"},
    },
    tags=["customer-card"],
    summary="Get list of customer cards",
    response_model_by_alias=True,
)
async def get_customer_card_list(
    customer_card_criteria: CustomerCardCriteria = Body(None, description=""),
) -> CustomerCard:
    ...


@router.post(
    "/api/customer-card/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether customer card was updated"},
    },
    tags=["customer-card"],
    summary="Update existing customer card",
    response_model_by_alias=True,
)
async def update_customer_card(
    id: int = Path(..., description=""),
    customer_card_view: CustomerCardView = Body(None, description=""),
) -> bool:
    ...
