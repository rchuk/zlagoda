from typing import Dict

from openapi_server.apis.customer_card_api_base import BaseCustomerCardApi

from openapi_server.models.customer_card import CustomerCard
from openapi_server.models.customer_card_criteria import CustomerCardCriteria
from openapi_server.models.customer_card_list_response import CustomerCardListResponse
from openapi_server.models.customer_card_view import CustomerCardView


class CustomerCardApi(BaseCustomerCardApi):
    def __init__(self):
        self._customer_cards: Dict[int, CustomerCard] = {
            0: CustomerCard(
                id=0,
                first_name="Іван",
                last_name="Абрамов",
                patronymic="Ігорович",
                phone_number="+380974630000",
                discount_percent=20,
                city="Бровари",
                street="Головна",
                zip_code="55555"
            ),
            1: CustomerCard(
                id=1,
                first_name="Артем",
                last_name="Гречка",
                patronymic="Віталійович",
                phone_number="+380996840184",
                discount_percent=0,
                city="Київ",
                street="Вулиція Гетьмана Данила",
                zip_code="04555"
            )
        }

    def create_customer_card(
        self,
        customer_card_view: CustomerCardView,
    ) -> int:
        raise NotImplementedError()


    def delete_customer_card(
        self,
        id: int,
    ) -> bool:
        raise NotImplementedError()


    def get_customer_card_by_id(
        self,
        id: int,
    ) -> CustomerCard:
        return self._customer_cards[id]


    def get_customer_card_list(
        self,
        customer_card_criteria: CustomerCardCriteria,
    ) -> CustomerCardListResponse:
        return CustomerCardListResponse(totalCount=len(self._customer_cards), items=list(self._customer_cards.values()))


    def update_customer_card(
        self,
        id: int,
        customer_card_view: CustomerCardView,
    ) -> bool:
        raise NotImplementedError()
