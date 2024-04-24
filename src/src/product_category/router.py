from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from product_category.schemas import (
    ProductCategoryCriteria,
    ProductCategoryUpsertRequest,
    ProductCategoryResponse,
    ProductCategoryListResponse
)

router = APIRouter()


@router.post("/api/product-category")
async def create_product_category(
    product_category_upsert_request: Annotated[ProductCategoryUpsertRequest | None, Body()] = None
) -> int:
    pass


@router.delete("/api/product-category/{id}")
async def delete_product_category(
    id: Annotated[int, Path()]
) -> bool:
    pass


@router.get("/api/product-category/{id}", response_model=ProductCategoryResponse)
async def get_product_category_by_id(
    id: Annotated[int, Path()]
) -> ProductCategoryResponse:
    pass


@router.post("/api/product-category/list", response_model=ProductCategoryListResponse)
async def get_product_category_list(
    product_category_criteria: Annotated[ProductCategoryCriteria | None, Body()] = None
) -> ProductCategoryListResponse:
    pass


@router.put("/api/product-category/{id}")
async def update_product_category(
    id: Annotated[int, Path()],
    product_category_upsert_request: Annotated[ProductCategoryUpsertRequest | None, Body()] = None
) -> bool:
    pass
