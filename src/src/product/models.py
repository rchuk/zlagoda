from decimal import Decimal

from pydantic import BaseModel


class Product(BaseModel):
    upc: str
    discount_id: str | None = None
    archetype: int
    price: Decimal
    quantity: int
    has_discount: bool
