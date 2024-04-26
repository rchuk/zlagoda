from product_archetype.schemas import (
    ProductArchetypeUpsertRequest,
    ProductArchetypeResponse,
    ProductArchetypeListResponse
)

from product_archetype.models import ProductArchetype


async def upsert_request_to_model(product_archetype: ProductArchetypeUpsertRequest) -> ProductArchetype:
    return ProductArchetype.model_construct(
        category=product_archetype.category,
        name=product_archetype.name,
        manufacturer=product_archetype.manufacturer,
        description=product_archetype.description
    )


async def model_to_response(product_archetype: ProductArchetype) -> ProductArchetypeResponse:
    return ProductArchetypeResponse.model_construct(
        id=product_archetype.id,
        category=product_archetype.category,
        name=product_archetype.name,
        manufacturer=product_archetype.manufacturer,
        description=product_archetype.description
    )


async def model_list_to_response_list(employee_list: list[ProductArchetype], count: int) -> ProductArchetypeListResponse:
    return ProductArchetypeListResponse.model_construct(
        totalCount=count,
        items=[await model_to_response(model) for model in employee_list]
    )
