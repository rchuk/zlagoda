from customer_card.schemas import (
    CustomerCardUpsertRequest,
    CustomerCardResponse,
    CustomerCardListResponse
)

from customer_card.models import CustomerCard


async def upsert_request_to_model(customer_card: CustomerCardUpsertRequest) -> CustomerCard:
    return CustomerCard.model_construct(
        last_name=customer_card.last_name,
        first_name=customer_card.first_name,
        patronymic=customer_card.patronymic,
        phone_number=customer_card.phone_number,
        city=customer_card.city,
        street=customer_card.street,
        zip_code=customer_card.zip_code,
        discount_percent=customer_card.discount_percent
    )


async def model_to_response(customer_card: CustomerCard) -> CustomerCardResponse:
    return CustomerCardResponse.model_construct(
        id=customer_card.id,
        lastName=customer_card.last_name,
        firstName=customer_card.first_name,
        patronymic=customer_card.patronymic,
        phoneNumber=customer_card.phone_number,
        city=customer_card.city,
        street=customer_card.street,
        zipCode=customer_card.zip_code,
        discountPercent=customer_card.discount_percent
    )


async def model_list_to_response_list(customer_card_list: list[CustomerCard], count: int) -> CustomerCardListResponse:
    return CustomerCardListResponse.model_construct(
        totalCount=count,
        items=[await model_to_response(model) for model in customer_card_list]
    )
