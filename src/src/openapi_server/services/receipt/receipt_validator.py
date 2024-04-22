from datetime import datetime

from openapi_server.entities.customer_card_entity import CustomerCardEntity
from openapi_server.entities.employee_entity import EmployeeEntity
from openapi_server.entities.receipt_entity import ReceiptEntity
from openapi_server.exceptions.app_exception import AppException
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase
from openapi_server.services.base.validator_base import ValidatorBase


class ReceiptValidator(ValidatorBase[ReceiptEntity]):
    def __init__(
        self,
        receipt_repository: CrudRepositoryBase[int, ReceiptEntity],
        employee_repository: CrudRepositoryBase[int, EmployeeEntity],
        customer_card_repository: CrudRepositoryBase[int, CustomerCardEntity]
    ):
        self._receipt_repository = receipt_repository
        self._employee_repository = employee_repository
        self._customer_card_repository = customer_card_repository

    def validate_create(self, entity: ReceiptEntity):
        self.validate_fields(entity)

    def validate_update(self, entity: ReceiptEntity, id):
        self.validate_fields(entity)

    def validate_fields(self, entity: ReceiptEntity):
        if entity.customer_card_id is not None and self._customer_card_repository.get(entity.customer_card_id) is None:
            raise ValidationError("Вказаної картки клієнта не існує")

        if self._employee_repository.get(entity.cashier_id) is None:
            raise AppException("Employee doesn't exist")
        if entity.date_time > datetime.now():
            raise AppException("Receipt creation date can't be in future")
        if entity.total_price < 0:
            raise AppException("Receipt total price can't be negative")
        if entity.vat < 0:
            raise AppException("Receipt vat can't be negative")
