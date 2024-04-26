from product_category import repository
from product_category.schemas import (
    ProductCategoryCriteria,
    ProductCategoryUpsertRequest,
    ProductCategoryResponse,
    ProductCategoryListResponse
)

from product_category.converters import (
    upsert_request_to_model,
    model_to_response,
    model_list_to_response_list
)

from product_category.validators import validate_model, validate_exists


async def add_product_category(product_category: ProductCategoryUpsertRequest) -> int:
    product_category = await upsert_request_to_model(product_category)
    await validate_model(product_category)
    id = await repository.create(product_category)
    return id


async def get_product_category(id: int) -> ProductCategoryResponse:
    await validate_exists(id)
    result = await repository.read_one(id)
    result = await model_to_response(result)
    return result


async def list_product_categories(product_category_criteria: ProductCategoryCriteria) -> ProductCategoryListResponse:
    result_list = await repository.read(product_category_criteria)
    result_count = await repository.count(product_category_criteria)
    result = await model_list_to_response_list(result_list, result_count)
    return result


async def update_product_category(id: int, product_category: ProductCategoryUpsertRequest) -> bool:
    await validate_exists(id)
    product_category = await upsert_request_to_model(product_category)
    product_category.id = id
    await validate_model(product_category)
    success = await repository.update(product_category)
    return success


async def delete_product_category(id: int) -> bool:
    await validate_exists(id)
    success = await repository.delete(id)
    return success
