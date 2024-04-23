from pydantic import BaseModel

from models import BaseCriteria, ListResponse


class ProductCategoryBase(BaseModel):
    """
    Product Category Base
    """
    name: str


class ProductCategoryCriteria(BaseCriteria):
    """
    Product Category Criteria
    """
    ids: list[int] | None = None
    query: str | None = None


class ProductCategoryUpsertRequest(ProductCategoryBase):
    """
    Product Category Upsert Request
    """
    pass


class ProductCategoryResponse(ProductCategoryBase):
    """
    Product Category Response
    """
    id: int


class ProductCategoryListResponse(ListResponse):
    """
    Product Category List Response
    """
    items: list[ProductCategoryResponse]
