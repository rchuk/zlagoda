from pydantic import BaseModel


class ProductArchetype(BaseModel):
    id: int
    category: int
    name: str
    manufacturer: str
    description: str
