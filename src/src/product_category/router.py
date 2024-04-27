from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path, Security,
)

from auth.dependencies import current_user
from auth.schemas import UserResponse, UserRole
from product_category.schemas import (
    ProductCategoryCriteria,
    ProductCategoryUpsertRequest,
    ProductCategoryResponse,
    ProductCategoryListResponse
)

from product_category import service

router = APIRouter()


@router.post("/api/product-category")
async def create_product_category(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    product_category_upsert_request: Annotated[ProductCategoryUpsertRequest | None, Body()] = None
) -> int:
    return await service.add_product_category(product_category_upsert_request)


@router.delete("/api/product-category/{id}")
async def delete_product_category(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    id: Annotated[int, Path()]
) -> bool:
    return await service.delete_product_category(id)


@router.get("/api/product-category/{id}", response_model=ProductCategoryResponse)
async def get_product_category_by_id(
    user: Annotated[UserResponse, Security(current_user)],
    id: Annotated[int, Path()]
) -> ProductCategoryResponse:
    return await service.get_product_category(id)


@router.post("/api/product-category/list", response_model=ProductCategoryListResponse)
async def get_product_category_list(
    user: Annotated[UserResponse, Security(current_user)],
    product_category_criteria: Annotated[ProductCategoryCriteria | None, Body()] = None
) -> ProductCategoryListResponse:
    return await service.list_product_categories(product_category_criteria)


@router.put("/api/product-category/{id}")
async def update_product_category(
    user: Annotated[UserResponse, Security(current_user, scopes=[UserRole.MANAGER, UserRole.ADMIN])],
    id: Annotated[int, Path()],
    product_category_upsert_request: Annotated[ProductCategoryUpsertRequest | None, Body()] = None
) -> bool:
    return await service.update_product_category(id, product_category_upsert_request)
