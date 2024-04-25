from datetime import datetime

from pydantic import BaseModel


class ReceiptItem(BaseModel):
    upc: str
    receipt_id: int
    quantity: int
    price: int


class Receipt(BaseModel):
    id: int
    cashier_id: int
    customer_card_id: int | None = None
    date_time: datetime
    total_price: int
    vat: int
