# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.receipt_api_base import BaseReceiptApi
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
from openapi_server.models.receipt import Receipt
from openapi_server.models.receipt_criteria import ReceiptCriteria
from openapi_server.models.receipt_list_response import ReceiptListResponse
from openapi_server.models.receipt_view import ReceiptView


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.put(
    "/api/receipt",
    responses={
        200: {"model": int, "description": "Id of new receipt"},
    },
    tags=["receipt"],
    summary="Create a new receipt",
    response_model_by_alias=True,
)
async def create_receipt(
    receipt_view: ReceiptView = Body(None, description=""),
) -> int:
    """Create a new receipt"""
    return BaseReceiptApi.subclasses[0]().create_receipt(receipt_view)


@router.delete(
    "/api/receipt/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether receipt was deleted"},
    },
    tags=["receipt"],
    summary="Delete a receipt by id",
    response_model_by_alias=True,
)
async def delete_receipt(
    id: int = Path(..., description=""),
) -> bool:
    """Delete a receipt by id"""
    return BaseReceiptApi.subclasses[0]().delete_receipt(id)


@router.get(
    "/api/receipt/{id}",
    responses={
        200: {"model": Receipt, "description": "Receipt by id"},
    },
    tags=["receipt"],
    summary="Get receipt by id",
    response_model_by_alias=True,
)
async def get_receipt_by_id(
    id: int = Path(..., description=""),
) -> Receipt:
    """Get receipt by id"""
    return BaseReceiptApi.subclasses[0]().get_receipt_by_id(id)


@router.post(
    "/api/receipt",
    responses={
        200: {"model": ReceiptListResponse, "description": "List of receipts"},
    },
    tags=["receipt"],
    summary="Get list of receipts",
    response_model_by_alias=True,
)
async def get_receipt_list(
    receipt_criteria: ReceiptCriteria = Body(None, description=""),
) -> ReceiptListResponse:
    """Get list of receipts"""
    return BaseReceiptApi.subclasses[0]().get_receipt_list(receipt_criteria)
