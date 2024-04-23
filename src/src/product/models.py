from typing import Annotated

from pydantic import BaseModel, Field

from models import BaseCriteria, ListResponse


class ProductBase(BaseModel):
    id: str
    archetype: int
    price: int
    quantity: int


class ProductCriteria(BaseCriteria):
    ids: list[str] | None = None
    query: str | None = None
    category_ids: Annotated[list[int] | None, Field(alias="categoryIds")] = None
    name: str | None = None
    has_discount: Annotated[bool | None, Field(alias="hasDiscount")] = None


class ProductUpsertRequest(ProductBase):
    pass


class ProductResponse(ProductBase):
    discount_id: Annotated[str | None, Field(alias="discountId")] = None
    has_discount: Annotated[bool, Field(alias="hasDiscount")]


class ProductListResponse(ListResponse):
    items: list[ProductResponse]
