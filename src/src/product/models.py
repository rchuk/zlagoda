from typing import Annotated

from pydantic import BaseModel, Field

from models import BaseCriteria, ListResponse


class ProductBase(BaseModel):
    """
    Product Base
    """
    id: str
    archetype: int
    price: int
    quantity: int


class ProductCriteria(BaseCriteria):
    """
    Product Criteria
    """
    ids: list[str] | None = None
    query: str | None = None
    category_ids: Annotated[list[int] | None, Field(alias="categoryIds")] = None
    name: str | None = None
    has_discount: Annotated[bool | None, Field(alias="hasDiscount")] = None


class ProductUpsertRequest(ProductBase):
    """
    Product Upsert Request
    """
    pass


class ProductResponse(ProductBase):
    """
    Product Response
    """
    discount_id: Annotated[str | None, Field(alias="discountId")] = None
    has_discount: Annotated[bool, Field(alias="hasDiscount")]


class ProductListResponse(ListResponse):
    """
    Product List Response
    """
    items: list[ProductResponse]
