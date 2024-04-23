from dependency_injector.wiring import Provide, inject

from openapi_server.apis.receipt_api_base import BaseReceiptApi
from openapi_server.containers import ApplicationContainer

from openapi_server.models.receipt import Receipt
from openapi_server.models.receipt_criteria import ReceiptCriteria
from openapi_server.models.receipt_list_response import ReceiptListResponse
from openapi_server.models.receipt_view import ReceiptView
from openapi_server.services.receipt.receipt_service import ReceiptService


class ReceiptApi(BaseReceiptApi):
    @inject
    def __init__(
        self,
        receipt_service: ReceiptService = Provide[ApplicationContainer.services.receipt_service]
    ):
        self._service = receipt_service

    def create_receipt(
        self,
        receipt_view: ReceiptView,
    ) -> int:
        return self._service.create(receipt_view)

    def delete_receipt(
        self,
        id: int,
    ) -> bool:
        return self._service.delete(id)

    def get_receipt_by_id(
        self,
        id: int,
    ) -> Receipt:
        return self._service.get(id)

    def get_receipt_list(
        self,
        receipt_criteria: ReceiptCriteria,
    ) -> ReceiptListResponse:
        return ReceiptListResponse(
            totalCount=self._service.count(receipt_criteria),
            items=self._service.list(receipt_criteria)
        )
