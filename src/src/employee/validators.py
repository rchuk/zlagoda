from datetime import datetime

from employee.models import Employee
from . import repository
from employee.exceptions import EmployeeNotFoundException
from exceptions import ValidationError
from employee.utils import calculate_age


async def validate_model(model: Employee):
    if len(model.last_name) < 1:
        raise ValidationError("Прізвище повинне складатися хоча б з 1 символу")
    if len(model.last_name) > 50:
        raise ValidationError("Прізвище повинне бути коротше 50 символів")
    if len(model.first_name) < 1:
        raise ValidationError("Ім'я повинне складатися хоча б з 1 символу")
    if len(model.first_name) > 50:
        raise ValidationError("Ім'я повинне бути коротше 50 символів")
    if model.patronymic is not None:
        if len(model.patronymic) < 1:
            raise ValidationError("По-батькові повинне складатися хоча б з 1 символу")
        if len(model.patronymic) > 50:
            raise ValidationError("По-батькові повинне бути коротше 50 символів")
    if model.salary < 0:
        raise ValidationError("Зарплатня не може бути від'ємною")
    if model.birth_date > datetime.now().date():
        raise ValidationError("Дата народження не може бути у майбутньому")
    if calculate_age(model.birth_date) < 18:
        raise ValidationError("Вік працівника не може бути меншим за 18 років")
    if model.work_start_date > datetime.now().date():
        raise ValidationError("Дата початку роботи не може бути у майбутньому")
    if len(model.phone_number) < 1:
        raise ValidationError("Телефон повинен складатися хоча б з 1 символу")
    if len(model.phone_number) > 13:
        raise ValidationError("Телефон повинен бути коротше 13 символів")
    if model.city is not None:
        if len(model.city) < 1:
            raise ValidationError("Місто повинне складатися хоча б з 1 символу")
        if len(model.city) > 50:
            raise ValidationError("Місто повинне бути коротше 50 символів")
    if model.street is not None:
        if len(model.street) < 1:
            raise ValidationError("Вулиця повинна складатися хоча б з 1 символу")
        if len(model.street) > 50:
            raise ValidationError("Вулиця повинна бути коротше 50 символів")
    if model.zip_code is not None:
        if len(model.zip_code) < 1:
            raise ValidationError("Поштовий код повинен складатися хоча б з 1 символу")
        if len(model.zip_code) > 9:
            raise ValidationError("Поштовий код повинен бути коротше 9 символів")


async def validate_exists(id: str):
    model = await repository.read_one(id)
    if model is None:
        raise EmployeeNotFoundException()
