# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.receipt import Receipt
from openapi_server.models.receipt_criteria import ReceiptCriteria
from openapi_server.models.receipt_list_response import ReceiptListResponse
from openapi_server.models.receipt_view import ReceiptView


class BaseReceiptApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseReceiptApi.subclasses = BaseReceiptApi.subclasses + (cls,)
    def create_receipt(
        self,
        receipt_view: ReceiptView,
    ) -> int:
        ...


    def delete_receipt(
        self,
        id: int,
    ) -> bool:
        ...


    def get_receipt_by_id(
        self,
        id: int,
    ) -> Receipt:
        ...


    def get_receipt_list(
        self,
        receipt_criteria: ReceiptCriteria,
    ) -> ReceiptListResponse:
        ...
