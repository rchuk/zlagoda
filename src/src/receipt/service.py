from decimal import Decimal

from exceptions import ValidationError
from receipt import repository
from receipt.schemas import (
    ReceiptCriteria,
    ReceiptUpsertRequest,
    ReceiptResponse,
    ReceiptListResponse
)

from receipt.converters import (
    upsert_request_to_model,
    model_to_response,
    model_list_to_response_list
)

from receipt.validators import validate_model, validate_exists
from product.validators import validate_exists as product_validate_exists
from customer_card.validators import validate_exists as customer_card_validate_exists
from product import service as product_service
from product import repository as product_repository
from customer_card import service as customer_card_service
from utils import generate_random_str_id
from datetime import datetime, timezone

from auth.dependencies import current_user


async def add_receipt(cashier_id: str, receipt: ReceiptUpsertRequest) -> str:
    receipt, receipt_items_list = await upsert_request_to_model(receipt)
    receipt_id = generate_random_str_id(10)
    receipt.id = receipt_id
    discount = 1
    if receipt.customer_card_id is not None:
        await customer_card_validate_exists(receipt.customer_card_id)
        discount -= (await customer_card_service.get_customer_card(receipt.customer_card_id)).discount_percent / 100
    total_price = 0
    for item in receipt_items_list:
        item.receipt_id = receipt_id
        await product_validate_exists(item.upc)
        product = await product_service.get_product(item.upc)
        if item.quantity > product.quantity:
            raise ValidationError("Кількість продукту не може бути більшою, аніж є взагалі")
        item.price = product.price * Decimal(item.quantity) * Decimal(discount)
        if product.has_discount:
            item.price *= Decimal("0.8")
        total_price += item.price

    receipt.cashier_id = cashier_id
    receipt.date_time = datetime.now(timezone.utc)
    receipt.total_price = total_price
    receipt.vat = Decimal("0.2") * total_price

    await validate_model(receipt, receipt_items_list)
    id = await repository.create(receipt, receipt_items_list)
    for item in receipt_items_list:
        product = await product_repository.read_one(item.upc)
        product.quantity -= item.quantity
        await product_repository.update(product)
    return id


async def get_receipt(id: str) -> ReceiptResponse:
    await validate_exists(id)
    receipt, items = await repository.read_one(id)
    result = await model_to_response(receipt, items)
    return result


async def list_receipts(receipt_criteria: ReceiptCriteria) -> ReceiptListResponse:
    receipt_list, items_list = await repository.read(receipt_criteria)
    result_count = await repository.count(receipt_criteria)
    result_list = zip(receipt_list, items_list)
    result = await model_list_to_response_list(result_list, result_count)
    return result


async def delete_receipt(id: str) -> bool:
    await validate_exists(id)
    success = await repository.delete(id)
    return success
