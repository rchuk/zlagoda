from openapi_server.entities.product_entity import ProductEntity
from openapi_server.entities.receipt_entity import ReceiptEntity
from openapi_server.entities.receipt_item_entity import ReceiptItemEntity
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase
from openapi_server.services.base.merger_base import MergerBase


class ReceiptItemMerger(MergerBase[ReceiptItemEntity, ReceiptItemEntity]):
    def __init__(
        self,
        product_repository: CrudRepositoryBase[str, ProductEntity],
        receipt_repository: CrudRepositoryBase[int, ReceiptEntity],
    ):
        self._product_repository = product_repository
        self._receipt_repository = receipt_repository

    def merge_create(self, entity: ReceiptItemEntity, view: ReceiptItemEntity):
        self._merge_main_fields(entity, view)

    def merge_edit(self, entity: ReceiptItemEntity, view: ReceiptItemEntity):
        self._merge_main_fields(entity, view)

    def _merge_main_fields(self, entity: ReceiptItemEntity, view: ReceiptItemEntity):
        product = self._product_repository.get(view.product)
        if product is None:
            raise ValidationError("Вказаного товару не існує")

        entity.product = view.product
        entity.receipt = view.receipt
        entity.price = product.price
        entity.quantity = view.quantity
