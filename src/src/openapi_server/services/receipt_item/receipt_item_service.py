from openapi_server.entities.product_entity import ProductEntity
from openapi_server.entities.receipt_item_entity import ReceiptItemEntity
from openapi_server.models.receipt_item import ReceiptItem
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

from openapi_server.services.base.crud_service_base import CrudServiceBase
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase


class ReceiptItemService(CrudServiceBase[int, ReceiptItemEntity, ReceiptItemEntity, ReceiptItem]):
    def __init__(
        self,
        repository: CrudRepositoryBase[id, ReceiptItemEntity],
        merger: MergerBase[ReceiptItemEntity, ReceiptItemEntity],
        validator: ValidatorBase[ReceiptItemEntity],
        product_repository: CrudRepositoryBase[str, ProductEntity]
    ):
        super().__init__(
            repository, merger, validator,
            lambda: ReceiptItemEntity.model_construct(),
            self.build_dto
        )
        self._product_repository = product_repository

    def build_dto(self, entity: ReceiptItemEntity) -> ReceiptItem:
        product = self._product_repository.get(entity.product)

        # TODO: Return UPC
        return ReceiptItem(
            product_archetype=product.archetype,
            quantity=entity.quantity,
            price=entity.price
        )
