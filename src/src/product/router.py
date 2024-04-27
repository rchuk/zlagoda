from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path, Security,
)

from auth.dependencies import current_user
from auth.schemas import UserResponse, UserRole
from product import service
from product.schemas import (
    ProductCriteria,
    ProductUpsertRequest,
    ProductResponse,
    ProductListResponse
)

router = APIRouter()


@router.post("/api/product")
async def create_product(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    product_upsert_request: Annotated[ProductUpsertRequest | None, Body()] = None
) -> str:
    return await service.add_product(product_upsert_request)


@router.delete("/api/product/{id}")
async def delete_product(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    id: Annotated[str, Path()]
) -> bool:
    return await service.delete_product_category(id)


@router.get("/api/product/{id}", response_model=ProductResponse)
async def get_product_by_id(
    user: Annotated[UserResponse, Security(current_user)],
    id: Annotated[str, Path()]
) -> ProductResponse:
    return await service.get_product(id)


@router.post("/api/product/list", response_model=ProductListResponse)
async def get_product_list(
    user: Annotated[UserResponse, Security(current_user)],
    product_criteria: Annotated[ProductCriteria | None, Body()] = None
) -> ProductListResponse:
    return await service.list_products(product_criteria)


@router.put("/api/product/{id}")
async def update_product(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    id: Annotated[str, Path()],
    product_upsert_request: Annotated[ProductUpsertRequest | None, Body()] = None
) -> bool:
    return await service.update_product(id, product_upsert_request)
