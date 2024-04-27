from receipt.schemas import (
    ReceiptUpsertRequest,
    ReceiptResponse,
    ReceiptListResponse,
    ReceiptItemResponse
)

from receipt.models import Receipt, ReceiptItem


async def upsert_request_to_model(receipt: ReceiptUpsertRequest) -> (Receipt, list[ReceiptItem]):
    receipt_items_list = []
    for item in receipt.items:
        receipt_items_list.append(ReceiptItem.model_construct(
            upc=item.product,
            quantity=item.quantity
        ))

    receipt = Receipt.model_construct(
        customer_card_id=receipt.customer_card_id
    )
    return receipt, receipt_items_list


async def model_to_response(receipt: Receipt, receipt_items: list[ReceiptItem]) -> ReceiptResponse:
    receipt_items_response = []
    for item in receipt_items:
        receipt_items_response.append(
            ReceiptItemResponse.model_construct(
                product=item.upc,
                quantity=item.quantity,
                price=item.price
            )
        )
    return ReceiptResponse.model_construct(
        id=receipt.id,
        cashierId=receipt.cashier_id,
        customerCardId=receipt.customer_card_id,
        dateTime=receipt.date_time,
        totalPrice=receipt.total_price,
        vat=receipt.vat,
        items=receipt_items_response
    )


async def model_list_to_response_list(receipt_list: list[tuple[Receipt, list[ReceiptItem]]], count: int) -> ReceiptListResponse:
    return ReceiptListResponse.model_construct(
        totalCount=count,
        items=[await model_to_response(receipt, receipt_items) for receipt, receipt_items in receipt_list]
    )
