from product_archetype.models import ProductArchetype
from . import repository
from product_archetype.exceptions import ProductArchetypeNotFoundException
import product_category.validators
from exceptions import ValidationError


async def validate_model(model: ProductArchetype):
    if len(model.name) < 1:
        raise ValidationError("Назва повинна складатися хоча б з 1 символу")
    if len(model.name) > 50:
        raise ValidationError("Назва повинна бути коротше 50 символів")
    if len(model.manufacturer) < 1:
        raise ValidationError("Назва виробника повинна складатися хоча б з 1 символу")
    if len(model.manufacturer) > 100:
        raise ValidationError("Назва виробника повинна бути коротше 100 символів")
    if len(model.description) < 1:
        raise ValidationError("Опис повинен складатися хоча б з 1 символу")
    if len(model.description) > 100:
        raise ValidationError("Опис повинен бути коротше 100 символів")

    await product_category.validators.validate_exists(model.category)


async def validate_exists(id: int):
    model = await repository.read_one(id)
    if model is None:
        raise ProductArchetypeNotFoundException()
