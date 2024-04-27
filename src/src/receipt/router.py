from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path, Security,
)

from auth.dependencies import current_user
from auth.schemas import UserResponse, UserRole
from receipt import service
from receipt.schemas import (
    ReceiptCriteria,
    ReceiptUpsertRequest,
    ReceiptResponse,
    ReceiptListResponse
)

router = APIRouter()


@router.post("/api/receipt")
async def create_receipt(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.CASHIER, UserRole.ADMIN])],
    receipt_upsert_request: Annotated[ReceiptUpsertRequest | None, Body()] = None
) -> str:
    return await service.add_receipt(user.employee_id, receipt_upsert_request)


@router.delete("/api/receipt/{id}")
async def delete_receipt(
    user: Annotated[UserResponse, Security(current_user)],
    id: Annotated[str, Path()]
) -> bool:
    return await service.delete_receipt(id)


@router.get("/api/receipt/{id}", response_model=ReceiptResponse)
async def get_receipt_by_id(
    user: Annotated[UserResponse, Security(current_user)],
    id: Annotated[str, Path()]
) -> ReceiptResponse:
    return await service.get_receipt(id)


@router.post("/api/receipt/list", response_model=ReceiptListResponse)
async def get_receipt_list(
    user: Annotated[UserResponse, Security(current_user)],
    receipt_criteria: Annotated[ReceiptCriteria | None, Body()] = None
) -> ReceiptListResponse:
    return await service.list_receipts(receipt_criteria)
