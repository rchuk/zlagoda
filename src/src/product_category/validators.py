from product_category.models import ProductCategory
from . import repository
from product_category.exceptions import ProductCategoryNotFoundException
from exceptions import ValidationError


async def validate_model(model: ProductCategory):
    if len(model.name) < 1:
        raise ValidationError("Назва повинна складатися хоча б з 1 символу")
    if len(model.name) > 50:
        raise ValidationError("Назва повинна бути коротше 50 символів")

async def validate_exists(id: str):
    model = await repository.read_one(id)
    if model is None:
        raise ProductCategoryNotFoundException()
