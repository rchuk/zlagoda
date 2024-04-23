from pydantic import BaseModel

from models import BaseCriteria, ListResponse


class ProductArchetypeBase(BaseModel):
    """
    Product Archetype Base
    """
    name: str
    category: int
    manufacturer: str
    description: str


class ProductArchetypeCriteria(BaseCriteria):
    """
    Product Archetype Criteria
    """
    ids: list[int] | None = None
    query: str | None = None


class ProductArchetypeUpsertRequest(ProductArchetypeBase):
    """
    Product Archetype Upsert Request
    """
    pass


class ProductArchetypeResponse(ProductArchetypeBase):
    """
    Product Archetype Response
    """
    id: int


class ProductArchetypeListResponse(ListResponse):
    """
    Product Archetype List Response
    """
    items: list[ProductArchetypeResponse]
