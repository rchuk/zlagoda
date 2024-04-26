from product import repository
from product.schemas import (
    ProductCriteria,
    ProductUpsertRequest,
    ProductResponse,
    ProductListResponse
)

from product.converters import (
    upsert_request_to_model,
    model_to_response,
    model_list_to_response_list
)

from product.validators import validate_model, validate_exists


async def add_product(product: ProductUpsertRequest) -> str:
    product = await upsert_request_to_model(product)
    criteria = ProductCriteria(archetype=product.archetype)
    same_products = await repository.read(criteria)
    for prev_product in same_products:
        prev_product.price = product.price
        if not prev_product.has_discount:
            prev_product.has_discount = True
            product.discount_id = prev_product.upc
        await repository.update(prev_product)
    await validate_model(product)
    id = await repository.create(product)
    return id


async def get_product(id: str) -> ProductResponse:
    await validate_exists(id)
    result = await repository.read_one(id)
    result = await model_to_response(result)
    return result


async def list_products(product_criteria: ProductCriteria) -> ProductListResponse:
    result_list = await repository.read(product_criteria)
    result_count = await repository.count(product_criteria)
    result = await model_list_to_response_list(result_list, result_count)
    return result


async def update_product(id: str, product: ProductUpsertRequest) -> bool:
    await validate_exists(id)
    product = await upsert_request_to_model(product)
    product.upc = id
    await validate_model(product)
    success = await repository.update(product)
    return success


async def delete_product_category(id: str) -> bool:
    await validate_exists(id)
    success = await repository.delete(id)
    return success
