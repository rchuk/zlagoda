from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from product_archetype.schemas import (
    ProductArchetypeCriteria,
    ProductArchetypeUpsertRequest,
    ProductArchetypeResponse,
    ProductArchetypeListResponse
)

router = APIRouter()


@router.post("/api/product-archetype")
async def create_product_archetype(
    product_archetype_upsert_request: Annotated[ProductArchetypeUpsertRequest | None, Body()] = None
) -> int:
    pass


@router.delete("/api/product-archetype/{id}")
async def delete_product_archetype(
    id: Annotated[int, Path()]
) -> bool:
    pass


@router.get("/api/product-archetype/{id}", response_model=ProductArchetypeResponse)
async def get_product_archetype_by_id(
    id: Annotated[int, Path()]
) -> ProductArchetypeResponse:
    pass


@router.post("/api/product-archetype/list", response_model=ProductArchetypeListResponse)
async def get_product_archetype_list(
    product_archetype_criteria: Annotated[ProductArchetypeCriteria | None, Body()] = None
) -> ProductArchetypeListResponse:
    pass


@router.put("/api/product-archetype/{id}")
async def update_product_archetype(
    id: Annotated[int, Path()],
    product_archetype_upsert_request: Annotated[ProductArchetypeUpsertRequest | None, Body()] = None
) -> bool:
    pass
