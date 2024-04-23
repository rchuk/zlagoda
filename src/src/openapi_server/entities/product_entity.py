from typing import Optional

from pydantic import BaseModel, StrictStr, StrictInt, StrictBool


class ProductEntity(BaseModel):
    id: StrictStr
    archetype: StrictInt
    price: StrictInt
    quantity: StrictInt
    discount_id: Optional[StrictStr]
    has_discount: StrictBool
