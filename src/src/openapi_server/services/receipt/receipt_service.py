from datetime import datetime

from openapi_server.entities.receipt_entity import ReceiptEntity
from openapi_server.entities.receipt_item_entity import ReceiptItemEntity
from openapi_server.exceptions.app_exception import AppException
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.models.receipt import Receipt
from openapi_server.models.receipt_view import ReceiptView
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

from openapi_server.services.base.crud_service_base import CrudServiceBase, IdT
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase
from openapi_server.services.receipt_item.receipt_item_service import ReceiptItemService


class ReceiptService(CrudServiceBase[int, ReceiptEntity, ReceiptEntity, Receipt]):
    def __init__(
        self,
        repository: CrudRepositoryBase[id, ReceiptEntity],
        merger: MergerBase[ReceiptEntity, ReceiptEntity],
        validator: ValidatorBase[ReceiptEntity],
        receipt_item_service: ReceiptItemService
    ):
        super().__init__(
            repository, merger, validator,
            lambda: ReceiptEntity.model_construct(id=-1),
            self._build_dto
        )
        self._receipt_item_service = receipt_item_service
        self._vat_percent = 0.2  # TODO: Use configurable value

    # TODO: Use transaction
    def create(self, view: ReceiptView) -> int:
        # TODO: Rethink
        if len(view.items) == 0:
            raise ValidationError("Відсутні товари у чеку")
        #

        internal_view = ReceiptEntity.model_construct(
            id=-1,
            cashier_id=0,  # TODO: Use login service
            customer_card_id=view.customer_card_id,
            date_time=datetime.now(),
            total_price=0,
            vat=0
        )

        id = super().create(internal_view)

        for receipt_item_view in view.items:
            internal_receipt_item_view = ReceiptItemEntity.model_construct(
                product=receipt_item_view.product,
                receipt=id,
                quantity=receipt_item_view.quantity
            )
            self._receipt_item_service.create(internal_receipt_item_view)

        total_price = 666  # TODO: Use receipt item repository to sum price
        update_internal_view = ReceiptEntity.model_construct(
            total_price=total_price,
            vat=int(total_price * self._vat_percent)
        )
        super().update(id, update_internal_view)

        return id

    def update(self, id: int, view: ReceiptView) -> bool:
        raise AppException("Receipt might not be updated")

    def _build_dto(self, entity: ReceiptEntity) -> Receipt:
        # TODO: FIX! Specify ids
        items = self._receipt_item_service.list(None)

        return Receipt(
            id=entity.id,
            cashier_id=entity.cashier_id,
            customer_card_id=entity.customer_card_id,
            date_time=entity.date_time,
            total_price=entity.total_price,
            vat=entity.vat,
            items=items
        )
