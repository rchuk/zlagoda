from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from receipt.schemas import (
    ReceiptCriteria,
    ReceiptUpsertRequest,
    ReceiptResponse,
    ReceiptListResponse
)

router = APIRouter()


@router.post("/api/receipt")
async def create_receipt(
    receipt_upsert_request: Annotated[ReceiptUpsertRequest | None, Body()] = None
) -> int:
    pass


@router.delete("/api/receipt/{id}")
async def delete_receipt(
    id: Annotated[int, Path()]
) -> bool:
    pass


@router.get("/api/receipt/{id}", response_model=ReceiptResponse)
async def get_receipt_by_id(
    id: Annotated[int, Path()]
) -> ReceiptResponse:
    pass


@router.post("/api/receipt/list", response_model=ReceiptListResponse)
async def get_receipt_list(
    receipt_criteria: Annotated[ReceiptCriteria | None, Body()] = None
) -> ReceiptListResponse:
    pass
