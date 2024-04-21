from typing import Dict, List  # noqa: F401

from openapi_server.apis.customer_card_api_base import BaseCustomerCardApi

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
from openapi_server.models.customer_card_list_response import CustomerCardListResponse
from openapi_server.models.customer_card_view import CustomerCardView


router = APIRouter()


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
    """Create a new customer card"""
    return BaseCustomerCardApi.subclasses[0]().create_customer_card(customer_card_view)


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
    """Delete a customer card by id"""
    return BaseCustomerCardApi.subclasses[0]().delete_customer_card(id)


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
    """Get customer card by id"""
    return BaseCustomerCardApi.subclasses[0]().get_customer_card_by_id(id)


@router.post(
    "/api/customer-card",
    responses={
        200: {"model": CustomerCardListResponse, "description": "List of customer cards"},
    },
    tags=["customer-card"],
    summary="Get list of customer cards",
    response_model_by_alias=True,
)
async def get_customer_card_list(
    customer_card_criteria: CustomerCardCriteria = Body(None, description=""),
) -> CustomerCardListResponse:
    """Get list of customer cards"""
    return BaseCustomerCardApi.subclasses[0]().get_customer_card_list(customer_card_criteria)


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
    """Update existing customer card"""
    return BaseCustomerCardApi.subclasses[0]().update_customer_card(id, customer_card_view)
