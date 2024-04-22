import re

from openapi_server.entities.customer_card_entity import CustomerCardEntity
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.services.base.validator_base import ValidatorBase


class CustomerCardValidator(ValidatorBase[CustomerCardEntity]):
    def validate_create(self, entity: CustomerCardEntity):
        self.validate_fields(entity)

    def validate_update(self, entity: CustomerCardEntity, id):
        self.validate_fields(entity)

    def validate_fields(self, entity: CustomerCardEntity):
        if len(entity.first_name) == 0:
            raise ValidationError("Ім'я не може бути порожнім")
        if len(entity.last_name) == 0:
            raise ValidationError("Прізвище не може бути порожнім")
        if not re.fullmatch(r"^\+?3?8?(0\d{9})$", entity.phone_number):
            raise ValidationError("Неправильний номер телефону")
        if entity.discount_percent < 0:
            raise ValidationError("Знижка не може бути від'ємною")
        if entity.discount_percent > 100:
            raise ValidationError("Знижка не може бути більшою за 100%")
        # TODO: Use regex
        if entity.zip_code is not None and len(entity.zip_code) > 9:
            raise ValidationError("Неправильний поштовий індекс")
