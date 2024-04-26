from product.schemas import (
    ProductUpsertRequest,
    ProductResponse,
    ProductListResponse
)

from product.models import Product


async def upsert_request_to_model(product: ProductUpsertRequest) -> Product:
    return Product.model_construct(
        upc=product.id,
        archetype=product.archetype,
        price=product.price,
        quantity=product.quantity,
        has_discount=False
    )


async def model_to_response(product: Product) -> ProductResponse:
    return ProductResponse.model_construct(
        id=product.upc,
        archetype=product.archetype,
        price=product.price,
        quantity=product.quantity,
        discountId=product.discount_id,
        hasDiscount=product.has_discount
    )


async def model_list_to_response_list(product_list: list[Product], count: int) -> ProductListResponse:
    return ProductListResponse.model_construct(
        totalCount=count,
        items=[await model_to_response(model) for model in product_list]
    )
