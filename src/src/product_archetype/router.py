from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path, Security,
)

from auth.dependencies import current_user
from auth.schemas import UserResponse, UserRole
from product_archetype.schemas import (
    ProductArchetypeCriteria,
    ProductArchetypeUpsertRequest,
    ProductArchetypeResponse,
    ProductArchetypeListResponse
)

from product_archetype import service

router = APIRouter()


@router.post("/api/product-archetype")
async def create_product_archetype(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    product_archetype_upsert_request: Annotated[ProductArchetypeUpsertRequest | None, Body()] = None
) -> int:
    return await service.add_archetype(product_archetype_upsert_request)


@router.delete("/api/product-archetype/{id}")
async def delete_product_archetype(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    id: Annotated[int, Path()]
) -> bool:
    return await service.delete_product_archetype(id)


@router.get("/api/product-archetype/{id}", response_model=ProductArchetypeResponse)
async def get_product_archetype_by_id(
    user: Annotated[UserResponse, Security(current_user)],
    id: Annotated[int, Path()]
) -> ProductArchetypeResponse:
    return await service.get_product_archetype(id)


@router.post("/api/product-archetype/list", response_model=ProductArchetypeListResponse)
async def get_product_archetype_list(
    user: Annotated[UserResponse, Security(current_user)],
    product_archetype_criteria: Annotated[ProductArchetypeCriteria | None, Body()] = None
) -> ProductArchetypeListResponse:
    return await service.list_product_archetypes(product_archetype_criteria)


@router.put("/api/product-archetype/{id}")
async def update_product_archetype(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    id: Annotated[int, Path()],
    product_archetype_upsert_request: Annotated[ProductArchetypeUpsertRequest | None, Body()] = None
) -> bool:
    return await service.update_product_archetype(id, product_archetype_upsert_request)
