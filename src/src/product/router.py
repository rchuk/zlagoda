from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from product.models import (
    ProductCriteria,
    ProductUpsertRequest,
    ProductResponse,
    ProductListResponse
)

router = APIRouter()


@router.post("/api/product")
async def create_product(
    product_upsert_request: Annotated[ProductUpsertRequest | None, Body()] = None
) -> int:
    pass


@router.delete("/api/product/{id}")
async def delete_product(
    id: Annotated[int, Path()]
) -> bool:
    pass


@router.get("/api/product/{id}", response_model=ProductResponse)
async def get_product_by_id(
    id: Annotated[int, Path()]
) -> ProductResponse:
    pass


@router.post("/api/product/list", response_model=ProductListResponse)
async def get_product_list(
    product_criteria: Annotated[ProductCriteria | None, Body()] = None
) -> ProductListResponse:
    pass


@router.put("/api/product/{id}")
async def update_product(
    id: Annotated[int, Path()],
    product_upsert_request: Annotated[ProductUpsertRequest | None, Body()] = None
) -> bool:
    pass
