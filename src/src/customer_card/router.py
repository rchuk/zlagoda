from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from customer_card.schemas import (
    CustomerCardCriteria,
    CustomerCardUpsertRequest,
    CustomerCardResponse,
    CustomerCardListResponse
)

from customer_card import service

router = APIRouter()


@router.post("/api/customer-card")
async def create_customer_card(
    customer_card_upsert_request: Annotated[CustomerCardUpsertRequest | None, Body()] = None
) -> str:
    return await service.add_customer_card(customer_card_upsert_request)


@router.delete("/api/customer-card/{id}")
async def delete_customer_card(
    id: Annotated[str, Path()]
) -> bool:
    return await service.delete_customer_card(id)


@router.get("/api/customer-card/{id}", response_model=CustomerCardResponse)
async def get_customer_card_by_id(
    id: Annotated[str, Path()]
) -> CustomerCardResponse:
    return await service.get_customer_card(id)


@router.post("/api/customer-card/list", response_model=CustomerCardListResponse)
async def get_customer_card_list(
    customer_card_criteria: Annotated[CustomerCardCriteria | None,  Body()] = None
) -> CustomerCardListResponse:
    return await service.list_customer_cards(customer_card_criteria)


@router.put("/api/customer-card/{id}")
async def update_customer_card(
    id: Annotated[str, Path()],
    customer_card_upsert_request: Annotated[CustomerCardUpsertRequest | None, Body()] = None
) -> bool:
    return await service.update_customer_card(id, customer_card_upsert_request)
