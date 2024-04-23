from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from models import BaseCriteria, ListResponse


class ReceiptItemBase(BaseModel):
    quantity: int


class ReceiptItemUpsertRequest(ReceiptItemBase):
    product: str


class ReceiptItemResponse(ReceiptItemBase):
    product_archetype: Annotated[int, Field(alias="productArchetype")]
    price: int


class ReceiptBase(BaseModel):
    customer_card_id: Annotated[int | None, Field(alias="customerCardId")] = None


class ReceiptCriteria(BaseCriteria):
    ids: list[int] | None = None
    query: str | None = None
    cashier_ids: Annotated[list[int] | None, Field(alias="cashierIds")] = None
    start_date: Annotated[datetime | None, Field(alias="startDate")] = None
    end_date: Annotated[datetime | None, Field(alias="endDate")] = None


class ReceiptUpsertRequest(ReceiptBase):
    items: list[ReceiptItemUpsertRequest]


class ReceiptResponse(ReceiptBase):
    id: int
    cashier_id: Annotated[int, Field(alias="cashierId")]
    date_time: Annotated[datetime, Field(alias="dateTime")]
    total_price: Annotated[int, Field(alias="totalPrice")]
    vat: int
    items: list[ReceiptItemResponse]


class ReceiptListResponse(ListResponse):
    items: list[ReceiptResponse]
