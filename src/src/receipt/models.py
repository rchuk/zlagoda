from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from models import BaseCriteria, ListResponse


class ReceiptItemBase(BaseModel):
    """
    Receipt Item Base
    """
    quantity: int


class ReceiptItemUpsertRequest(ReceiptItemBase):
    """
    Receipt Item Upsert Request
    """
    product: str


class ReceiptItemResponse(ReceiptItemBase):
    """
    Receipt Item Response
    """
    product_archetype: Annotated[int, Field(alias="productArchetype")]
    price: int


class ReceiptBase(BaseModel):
    """
    Receipt Base
    """
    customer_card_id: Annotated[int | None, Field(alias="customerCardId")] = None


class ReceiptCriteria(BaseCriteria):
    """
    Receipt Criteria
    """
    ids: list[int] | None = None
    query: str | None = None
    cashier_ids: Annotated[list[int] | None, Field(alias="cashierIds")] = None
    start_date: Annotated[datetime | None, Field(alias="startDate")] = None
    end_date: Annotated[datetime | None, Field(alias="endDate")] = None


class ReceiptUpsertRequest(ReceiptBase):
    """
    Receipt Upsert Request
    """
    items: list[ReceiptItemUpsertRequest]


class ReceiptResponse(ReceiptBase):
    """
    Receipt Response
    """
    id: int
    cashier_id: Annotated[int, Field(alias="cashierId")]
    date_time: Annotated[datetime, Field(alias="dateTime")]
    total_price: Annotated[int, Field(alias="totalPrice")]
    vat: int
    items: list[ReceiptItemResponse]


class ReceiptListResponse(ListResponse):
    """
    Receipt List Response
    """
    items: list[ReceiptResponse]
