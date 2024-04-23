from pydantic import BaseModel, StrictStr, StrictInt


class ProductArchetypeEntity(BaseModel):
    id: StrictInt
    name: StrictStr
    category: StrictInt
    manufacturer: StrictStr
    description: StrictStr
