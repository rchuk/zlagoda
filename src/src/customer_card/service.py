from customer_card import repository
from customer_card.schemas import (
    CustomerCardCriteria,
    CustomerCardUpsertRequest,
    CustomerCardResponse,
    CustomerCardListResponse
)

from customer_card.converters import (
    upsert_request_to_model,
    model_to_response,
    model_list_to_response_list
)

from customer_card.validators import validate_model, validate_exists


async def add_customer_card(customer_card: CustomerCardUpsertRequest) -> str:
    customer_card = await upsert_request_to_model(customer_card)
    await validate_model(customer_card)
    id = await repository.create(customer_card)
    return id


async def get_customer_card(id: str) -> CustomerCardResponse:
    await validate_exists(id)
    result = await repository.read_one(id)
    result = await model_to_response(result)
    return result


async def list_customer_cards(customer_card_criteria: CustomerCardCriteria) -> CustomerCardListResponse:
    result_list = await repository.read(customer_card_criteria)
    result_count = await repository.count(customer_card_criteria)
    result = await model_list_to_response_list(result_list, result_count)
    return result


async def update_customer_card(id: str, customer_card: CustomerCardUpsertRequest) -> bool:
    await validate_exists(id)
    customer_card = await upsert_request_to_model(customer_card)
    customer_card.id = id
    await validate_model(customer_card)
    success = await repository.update(customer_card)
    return success


async def delete_customer_card(id: str) -> bool:
    await validate_exists(id)
    success = await repository.delete(id)
    return success
