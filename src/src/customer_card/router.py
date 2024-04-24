from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from customer_card.models import (
    CustomerCardCriteria,
    CustomerCardUpsertRequest,
    CustomerCardResponse,
    CustomerCardListResponse
)

router = APIRouter()


@router.post("/api/customer-card")
async def create_customer_card(
    customer_card_upsert_request: Annotated[CustomerCardUpsertRequest | None, Body()] = None
) -> int:
    pass


@router.delete("/api/customer-card/{id}")
async def delete_customer_card(
    id: Annotated[int, Path()]
) -> bool:
    pass


@router.get("/api/customer-card/{id}", response_model=CustomerCardResponse)
async def get_customer_card_by_id(
    id: Annotated[int, Path()]
) -> CustomerCardResponse:
    pass


@router.post("/api/customer-card/list", response_model=CustomerCardListResponse)
async def get_customer_card_list(
    customer_card_criteria: Annotated[CustomerCardCriteria | None,  Body()] = None
) -> CustomerCardListResponse:
    pass


@router.put("/api/customer-card/{id}")
async def update_customer_card(
    id: Annotated[int, Path()],
    customer_card_upsert_request: Annotated[CustomerCardUpsertRequest | None, Body()] = None
) -> bool:
    pass
