from customer_card import repository
from customer_card.schemas import (
    CustomerCardCriteria,
    CustomerCardUpsertRequest,
    CustomerCardResponse,
    CustomerCardListResponse
)

from customer_card.dependencies import (
    upsert_request_to_model,
    model_to_response,
    model_list_to_response_list
)


async def add_customer_card(customer_card: CustomerCardUpsertRequest) -> int:
    customer_card = await upsert_request_to_model(customer_card)
    id = await repository.create(customer_card)
    return id


async def get_customer_card(id: int) -> CustomerCardResponse:
    result = await repository.read_one(id)
    result = await model_to_response(result)
    return result


async def list_customer_cards(customer_card_criteria: CustomerCardCriteria) -> CustomerCardListResponse:
    result_list = await repository.read(customer_card_criteria)
    result_count = await repository.count(customer_card_criteria)
    result = await model_list_to_response_list(result_list, result_count)
    return result


async def update_customer_card(id: int, customer_card: CustomerCardUpsertRequest) -> bool:
    customer_card = await upsert_request_to_model(customer_card)
    customer_card.id = id
    success = await repository.update(customer_card)
    return success


async def delete_customer_card(id: int) -> bool:
    success = await repository.delete(id)
    return success
