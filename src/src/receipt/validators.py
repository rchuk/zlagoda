from datetime import datetime, timezone

from receipt.models import Receipt, ReceiptItem
from . import repository
from exceptions import ValidationError
from .exceptions import ReceiptNotFound


async def validate_model(receipt_model: Receipt, receipt_item_models:  list[ReceiptItem]):
    if receipt_model.date_time > datetime.now(timezone.utc):
        raise ValidationError("Дата створення чеку не може бути у майбутньому")
    if receipt_model.total_price < 0:
        raise ValidationError("Сума чеку не може бути від'ємною")
    if receipt_model.vat < 0:
        raise ValidationError("ПДВ не може бути від'ємним")
    for item in receipt_item_models:
        if item.price < 0:
            raise ValidationError("Вартість товару не може бути від'ємною")
        if item.quantity <= 0:
            raise ValidationError("Кількість товару має бути додатною")


async def validate_exists(id: str):
    model = await repository.read_one(id)
    if model is None:
        raise ReceiptNotFound()
