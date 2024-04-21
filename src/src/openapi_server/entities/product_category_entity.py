from pydantic import BaseModel, StrictStr, StrictInt


class ProductCategoryEntity(BaseModel):
    id: StrictInt
    name: StrictStr
