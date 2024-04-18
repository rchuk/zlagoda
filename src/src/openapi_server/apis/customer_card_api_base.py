# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.customer_card import CustomerCard
from openapi_server.models.customer_card_criteria import CustomerCardCriteria
from openapi_server.models.customer_card_view import CustomerCardView


class BaseCustomerCardApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCustomerCardApi.subclasses = BaseCustomerCardApi.subclasses + (cls,)
    def create_customer_card(
        self,
        customer_card_view: CustomerCardView,
    ) -> int:
        """Create a new customer card"""
        ...


    def delete_customer_card(
        self,
        id: int,
    ) -> bool:
        """Delete a customer card by id"""
        ...


    def get_customer_card_by_id(
        self,
        id: int,
    ) -> CustomerCard:
        """Get customer card by id"""
        ...


    def get_customer_card_list(
        self,
        customer_card_criteria: CustomerCardCriteria,
    ) -> CustomerCard:
        """Get list of customer cards"""
        ...


    def update_customer_card(
        self,
        id: int,
        customer_card_view: CustomerCardView,
    ) -> bool:
        """Update existing customer card"""
        ...
