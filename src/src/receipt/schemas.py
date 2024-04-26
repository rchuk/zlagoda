from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from schemas import BaseCriteria, ListResponse


class ReceiptItemBase(BaseModel):
    quantity: int


class ReceiptItemUpsertRequest(ReceiptItemBase):
    product: str


class ReceiptItemResponse(ReceiptItemBase):
    product_archetype: Annotated[int, Field(alias="productArchetype")]
    price: float


class ReceiptBase(BaseModel):
    customer_card_id: Annotated[str | None, Field(alias="customerCardId")] = None


class ReceiptCriteria(BaseCriteria):
    ids: list[str] | None = None
    query: str | None = None
    cashier_ids: Annotated[list[str] | None, Field(alias="cashierIds")] = None
    start_date: Annotated[datetime | None, Field(alias="startDate")] = None
    end_date: Annotated[datetime | None, Field(alias="endDate")] = None


class ReceiptUpsertRequest(ReceiptBase):
    items: list[ReceiptItemUpsertRequest]


class ReceiptResponse(ReceiptBase):
    id: str
    cashier_id: Annotated[str, Field(alias="cashierId")]
    date_time: Annotated[datetime, Field(alias="dateTime")]
    total_price: Annotated[float, Field(alias="totalPrice")]
    vat: float
    items: list[ReceiptItemResponse]


class ReceiptListResponse(ListResponse):
    items: list[ReceiptResponse]
