from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class ReceiptItem(BaseModel):
    upc: str
    receipt_id: str
    quantity: int
    price: Decimal


class Receipt(BaseModel):
    id: str
    cashier_id: str
    customer_card_id: str | None = None
    date_time: datetime
    total_price: Decimal
    vat: Decimal
