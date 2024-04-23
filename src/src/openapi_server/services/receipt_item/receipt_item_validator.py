from openapi_server.entities.product_entity import ProductEntity
from openapi_server.entities.receipt_entity import ReceiptEntity
from openapi_server.entities.receipt_item_entity import ReceiptItemEntity
from openapi_server.exceptions.app_exception import AppException
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase
from openapi_server.services.base.validator_base import ValidatorBase


class ReceiptItemValidator(ValidatorBase[ReceiptItemEntity]):
    def __init__(
        self,
        product_repository: CrudRepositoryBase[str, ProductEntity],
        receipt_repository: CrudRepositoryBase[int, ReceiptEntity],
    ):
        self._product_repository = product_repository
        self._receipt_repository = receipt_repository

    def validate_create(self, entity: ReceiptItemEntity):
        self.validate_fields(entity)

    def validate_update(self, entity: ReceiptItemEntity, id):
        raise AppException("ReceiptItem might not be edited")

    def validate_fields(self, entity: ReceiptItemEntity):
        if self._product_repository.get(entity.product) is None:
            raise ValidationError("Вказаного товару не існує")
        if self._receipt_repository.get(entity.receipt) is None:
            raise ValidationError("Вказаного чеку не існує")
        if entity.quantity < 0:
            raise ValidationError("Кількість не може бути від'ємною")

        if entity.price < 0:
            raise AppException("ReceiptItem price can't be negative")
