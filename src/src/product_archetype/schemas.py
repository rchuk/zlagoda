from pydantic import BaseModel

from schemas import BaseCriteria, ListResponse


class ProductArchetypeBase(BaseModel):
    name: str
    category: int
    manufacturer: str
    description: str


class ProductArchetypeCriteria(BaseCriteria):
    ids: list[int] | None = None
    query: str | None = None


class ProductArchetypeUpsertRequest(ProductArchetypeBase):
    pass


class ProductArchetypeResponse(ProductArchetypeBase):
    id: int


class ProductArchetypeListResponse(ListResponse):
    items: list[ProductArchetypeResponse]
