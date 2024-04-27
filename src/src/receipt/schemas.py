from datetime import datetime
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field

from schemas import BaseCriteria, ListResponse


class ReceiptItemBase(BaseModel):
    quantity: int
    product: str


class ReceiptItemUpsertRequest(ReceiptItemBase):
    pass


class ReceiptItemResponse(ReceiptItemBase):
    price: Decimal


class ReceiptBase(BaseModel):
    customer_card_id: Annotated[str | None, Field(alias="customerCardId")] = None


class ReceiptCriteria(BaseCriteria):
    ids: list[str] | None = None
    cashier_id: Annotated[str | None, Field(alias="cashierId")] = None
    start_date: Annotated[datetime | None, Field(alias="startDate")] = None
    end_date: Annotated[datetime | None, Field(alias="endDate")] = None


class ReceiptUpsertRequest(ReceiptBase):
    items: list[ReceiptItemUpsertRequest]


class ReceiptResponse(ReceiptBase):
    id: str
    cashier_id: Annotated[str, Field(alias="cashierId")]
    date_time: Annotated[datetime, Field(alias="dateTime")]
    total_price: Annotated[Decimal, Field(alias="totalPrice")]
    vat: Decimal
    items: list[ReceiptItemResponse]


class ReceiptListResponse(ListResponse):
    items: list[ReceiptResponse]
