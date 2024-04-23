from datetime import datetime

from openapi_server.entities.receipt_entity import ReceiptEntity
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase
from openapi_server.services.base.merger_base import MergerBase


class ReceiptMerger(MergerBase[ReceiptEntity, ReceiptEntity]):
    def __init__(
        self,
        product_repository: CrudRepositoryBase[str, ReceiptEntity],
        receipt_repository: CrudRepositoryBase[int, ReceiptEntity],
    ):
        self._product_repository = product_repository
        self._receipt_repository = receipt_repository

    def merge_create(self, entity: ReceiptEntity, view: ReceiptEntity):
        entity.cashier_id = view.cashier_id
        entity.customer_card_id = view.customer_card_id
        entity.date_time = datetime.now()

        self._merge_price(entity, view)

    def merge_edit(self, entity: ReceiptEntity, view: ReceiptEntity):
        self._merge_price(entity, view)

    def _merge_price(self, entity: ReceiptEntity, view: ReceiptEntity):
        entity.total_price = view.total_price
        entity.vat = view.vat
