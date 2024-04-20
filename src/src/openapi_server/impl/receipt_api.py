from datetime import datetime
from typing import Dict

from openapi_server.apis.receipt_api_base import BaseReceiptApi

from openapi_server.models.receipt import Receipt
from openapi_server.models.receipt_criteria import ReceiptCriteria
from openapi_server.models.receipt_item import ReceiptItem
from openapi_server.models.receipt_list_response import ReceiptListResponse
from openapi_server.models.receipt_view import ReceiptView


class ReceiptApi(BaseReceiptApi):
    def __init__(self):
        self._receipts: Dict[int, Receipt] = {
            0: Receipt(
                id=0,
                cashier_id=2,
                customer_card_id=1,
                date_time=datetime(2024, 4, 19, 12, 15, 33).date().isoformat(),
                total_price=1000,
                vat=34,
                items=[
                    ReceiptItem(
                        product_archetype=0,
                        quantity=100,
                        price=300
                    ),
                    ReceiptItem(
                        product_archetype=4,
                        quantity=1,
                        price=666
                    )
                ]
            ),
            1: Receipt(
                id=1,
                cashier_id=2,
                customer_card_id=None,
                date_time=datetime(2024, 4, 19, 10, 00, 00).date().isoformat(),
                total_price=205,
                vat=5,
                items=[
                    ReceiptItem(
                        product_archetype=0,
                        quantity=10,
                        price=100
                    ),
                    ReceiptItem(
                        product_archetype=1,
                        quantity=1,
                        price=100
                    )
                ]
            )
        }

    def create_receipt(
        self,
        receipt_view: ReceiptView,
    ) -> int:
        raise NotImplementedError()


    def delete_receipt(
        self,
        id: int,
    ) -> bool:
        raise NotImplementedError()


    def get_receipt_by_id(
        self,
        id: int,
    ) -> Receipt:
        return self._receipts[id]


    def get_receipt_list(
        self,
        receipt_criteria: ReceiptCriteria,
    ) -> ReceiptListResponse:
        return ReceiptListResponse(totalCount=len(self._receipts), items=list(self._receipts.values()))
