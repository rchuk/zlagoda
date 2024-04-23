from dependency_injector.wiring import Provide, inject

from openapi_server.apis.customer_card_api_base import BaseCustomerCardApi
from openapi_server.containers import ApplicationContainer

from openapi_server.models.customer_card import CustomerCard
from openapi_server.models.customer_card_criteria import CustomerCardCriteria
from openapi_server.models.customer_card_list_response import CustomerCardListResponse
from openapi_server.models.customer_card_view import CustomerCardView
from openapi_server.services.customer_card.customer_card_service import CustomerCardService


class CustomerCardApi(BaseCustomerCardApi):
    @inject
    def __init__(
        self,
        customer_card_service: CustomerCardService = Provide[ApplicationContainer.services.customer_card_service]
    ):
        self._service = customer_card_service

    def create_customer_card(
        self,
        customer_card_view: CustomerCardView,
    ) -> int:
        return self._service.create(customer_card_view)

    def delete_customer_card(
        self,
        id: int,
    ) -> bool:
        return self._service.delete(id)

    def get_customer_card_by_id(
        self,
        id: int,
    ) -> CustomerCard:
        return self._service.get(id)

    def get_customer_card_list(
        self,
        customer_card_criteria: CustomerCardCriteria,
    ) -> CustomerCardListResponse:
        return CustomerCardListResponse(
            totalCount=self._service.count(customer_card_criteria),
            items=self._service.list(customer_card_criteria)
        )

    def update_customer_card(
        self,
        id: int,
        customer_card_view: CustomerCardView,
    ) -> bool:
        return self._service.update(id, customer_card_view)
