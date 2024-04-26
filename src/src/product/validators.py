from exceptions import ValidationError
from product import repository
from product.exceptions import ProductNotFound
from product.models import Product


async def validate_model(model: Product):
    if len(model.upc) < 1:
        raise ValidationError("Код повинен складатися хоча б з 1 символу")
    if len(model.upc) > 12:
        raise ValidationError("Код повинен бути коротше 12 символів")
    if model.discount_id is not None:
        if len(model.discount_id) < 1:
            raise ValidationError("Код знижки повинен складатися хоча б з 1 символу")
        if len(model.discount_id) > 12:
            raise ValidationError("Код знижки повинен бути коротше 12 символів")
    if model.price < 0:
        raise ValidationError("Ціна повинна бути невід'ємною")
    if model.quantity < 0:
        raise ValidationError("Кількість повинна бути невід'ємною")


async def validate_exists(id: str):
    model = await repository.read_one(id)
    if model is None:
        raise ProductNotFound()
