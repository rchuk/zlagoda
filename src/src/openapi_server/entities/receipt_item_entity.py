from pydantic import BaseModel, StrictStr, StrictInt


class ReceiptItemEntity(BaseModel):
    product: StrictStr
    receipt: StrictInt
    price: StrictInt
    quantity: StrictInt
