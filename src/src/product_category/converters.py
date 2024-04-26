from product_category.schemas import (
    ProductCategoryUpsertRequest,
    ProductCategoryResponse,
    ProductCategoryListResponse
)

from product_category.models import ProductCategory


async def upsert_request_to_model(product_category: ProductCategoryUpsertRequest) -> ProductCategory:
    return ProductCategory.model_construct(
        name=product_category.name
    )


async def model_to_response(product_category: ProductCategory) -> ProductCategoryResponse:
    return ProductCategoryResponse.model_construct(
        id=product_category.id,
        name=product_category.name
    )


async def model_list_to_response_list(product_category_list: list[ProductCategory], count: int) -> ProductCategoryListResponse:
    return ProductCategoryListResponse.model_construct(
        totalCount=count,
        items=[await model_to_response(model) for model in product_category_list]
    )
