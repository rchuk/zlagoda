from pydantic import BaseModel

from schemas import BaseCriteria, ListResponse


class ProductCategoryBase(BaseModel):
    name: str


class ProductCategoryCriteria(BaseCriteria):
    ids: list[int] | None = None


class ProductCategoryUpsertRequest(ProductCategoryBase):
    pass


class ProductCategoryResponse(ProductCategoryBase):
    id: int


class ProductCategoryListResponse(ListResponse):
    items: list[ProductCategoryResponse]
