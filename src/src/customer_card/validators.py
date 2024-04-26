from customer_card.models import CustomerCard
from . import repository
from .exceptions import CustomerCardNotFound
from src.exceptions import ValidationError


async def validate_model(model: CustomerCard):
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
            raise ValidationError("Поштовий код повинен бути коротше 50 символів")
    if model.discount_percent < 0:
        raise ValidationError("Відсоток знижки не може бути від'ємним")


async def validate_exists(id: int):
    model = await repository.read_one(id)
    if model is None:
        raise CustomerCardNotFound()
