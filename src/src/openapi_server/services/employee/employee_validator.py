import re
from datetime import datetime

from openapi_server.entities.employee_entity import EmployeeEntity
from openapi_server.exceptions.validation_error import ValidationError
from openapi_server.services.base.validator_base import ValidatorBase


class EmployeeValidator(ValidatorBase[EmployeeEntity]):
    def validate_create(self, entity: EmployeeEntity):
        self.validate_fields(entity)

    def validate_update(self, entity: EmployeeEntity):
        self.validate_fields(entity)

    def validate_fields(self, entity: EmployeeEntity):
        if len(entity.first_name) == 0:
            raise ValidationError("Ім'я не може бути порожнім")
        if len(entity.last_name) == 0:
            raise ValidationError("Прізвище не може бути порожнім")
        if entity.salary < 0:
            raise ValidationError("Зарплатня не може бути від'ємною")
        if not re.fullmatch(r"^\+?3?8?(0\d{9})$", entity.phone_number):
            raise ValidationError("Неправильний номер телефону")
        if entity.work_start_date > datetime.today().date():
            raise ValidationError("Дата початку роботи не може бути у майбутньому")
        # TODO: Check that employee is over 18 years old (it's in the specification)
        if entity.birth_date > datetime.today().date():
            raise ValidationError("Дата народження не може бути у майбутньому")
        if len(entity.city) == 0:
            raise ValidationError("Місто не може бути порожнім")
        if len(entity.street) == 0:
            raise ValidationError("Вулиця не може бути порожньою")
        if len(entity.zip_code) == 0:
            raise ValidationError("Поштовий індекс не може бути порожнім")
        # TODO: Use regex
        if len(entity.zip_code) > 9:
            raise ValidationError("Неправильний поштовий індекс")