from pydantic import BaseModel

from models import BaseCriteria, ListResponse


class ProductCategoryBase(BaseModel):
    name: str


class ProductCategoryCriteria(BaseCriteria):
    ids: list[int] | None = None
    query: str | None = None


class ProductCategoryUpsertRequest(ProductCategoryBase):
    pass


class ProductCategoryResponse(ProductCategoryBase):
    id: int


class ProductCategoryListResponse(ListResponse):
    items: list[ProductCategoryResponse]
