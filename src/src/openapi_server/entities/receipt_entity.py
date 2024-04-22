from datetime import datetime
from typing import Optional

from pydantic import BaseModel, StrictInt


class ReceiptEntity(BaseModel):
    id: StrictInt
    cashier_id: StrictInt
    customer_card_id: Optional[StrictInt]
    date_time: datetime
    total_price: StrictInt
    vat: StrictInt
