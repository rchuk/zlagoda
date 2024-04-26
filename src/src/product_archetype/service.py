from product_archetype import repository
from product_archetype.schemas import (
    ProductArchetypeCriteria,
    ProductArchetypeUpsertRequest,
    ProductArchetypeResponse,
    ProductArchetypeListResponse
)

from product_archetype.converters import (
    upsert_request_to_model,
    model_to_response,
    model_list_to_response_list
)

from product_archetype.validators import validate_model, validate_exists


async def add_archetype(product_archetype: ProductArchetypeUpsertRequest) -> int:
    product_archetype = await upsert_request_to_model(product_archetype)
    await validate_model(product_archetype)
    id = await repository.create(product_archetype)
    return id


async def get_product_archetype(id: int) -> ProductArchetypeResponse:
    await validate_exists(id)
    result = await repository.read_one(id)
    result = await model_to_response(result)
    return result


async def list_product_archetypes(product_archetype_criteria: ProductArchetypeCriteria) -> ProductArchetypeListResponse:
    result_list = await repository.read(product_archetype_criteria)
    result_count = await repository.count(product_archetype_criteria)
    result = await model_list_to_response_list(result_list, result_count)
    return result


async def update_product_archetype(id: int, product_archetype: ProductArchetypeUpsertRequest) -> bool:
    await validate_exists(id)
    product_archetype = await upsert_request_to_model(product_archetype)
    product_archetype.id = id
    await validate_model(product_archetype)
    success = await repository.update(product_archetype)
    return success


async def delete_product_archetype(id: int) -> bool:
    await validate_exists(id)
    success = await repository.delete(id)
    return success
