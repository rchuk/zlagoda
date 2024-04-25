from pydantic import BaseModel


class Product(BaseModel):
    upc: str
    discount_id: str | None = None
    archetype: int
    price: int
    quantity: int
    has_discount: bool
