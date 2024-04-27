from psycopg import AsyncConnection
from psycopg.rows import class_row

from receipt.models import Receipt, ReceiptItem
from receipt.schemas import ReceiptCriteria
from database import db_conn
from exceptions import ValidationError
from utils import like_format
from product import repository as product_repository


def dto_field_to_entity_field(dto_field: str | None) -> str:
    if dto_field is None:
        return "id"

    fields = {
        "id": "id",
        "cashierId": "cashier_id",
        "customerCardId": "customer_card_id",
        "dateTime": "date_time",
        "totalPrice": "total_price",
        "vat": "vat"
    }

    entity_field = fields.get(dto_field)
    if entity_field is None:
        raise ValidationError("Вказане поле для сортування не вірне")

    return entity_field


async def create_item(item: ReceiptItem, conn: AsyncConnection):
    query = """
            INSERT INTO receipt_item(upc, receipt_id, quantity, price)
            VALUES (%(upc)s, %(receipt_id)s, %(quantity)s, %(price)s)
            """
    params = item.dict()
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    product = await product_repository.read_one(item.upc)
    product.quantity -= item.quantity
    await product_repository.update(item)


@db_conn
async def create(receipt: Receipt, items: list[ReceiptItem], conn: AsyncConnection) -> str:
    query = """
        INSERT INTO receipt(id, cashier_id, customer_card_id, date_time, total_price, vat)
        VALUES (%(id)s, %(cashier_id)s, %(customer_card_id)s, %(date_time)s, %(total_price)s, %(vat)s)
        RETURNING id;
        """
    params = receipt.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    for item in items:
        await create_item(item, conn)
    return res


async def read_items(receipt_id: str, conn: AsyncConnection) -> list[ReceiptItem]:
    query = f"""
            SELECT *
            FROM receipt_item 
            WHERE receipt_id = %s;
            """
    params = (receipt_id,)
    async with conn.cursor(row_factory=class_row(ReceiptItem)) as cur:
        res = await (await cur.execute(query, params)).fetchall()
    return res


@db_conn
async def read(criteria: ReceiptCriteria, conn: AsyncConnection) -> (list[Receipt], list[list[ReceiptItem]]):
    sort_field = dto_field_to_entity_field(criteria.sort_field)
    query = f"""
        SELECT *
        FROM receipt 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"date_time >= %(start_date)s" if criteria.start_date is not None else "TRUE"} AND 
        {"date_time <= %(end_date)s" if criteria.end_date is not None else "TRUE"} AND 
        {("(cashier_id LIKE %(query)s OR "
          "customer_card_id LIKE %(query)s)") if criteria.query is not None else "TRUE "}
        ORDER BY {sort_field} {'ASC ' if criteria.sort_ascending is None or criteria.sort_ascending else 'DESC '}
        {'LIMIT %(limit)s OFFSET %(offset)s ' if criteria.limit is not None and criteria.offset is not None else ''};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor(row_factory=class_row(Receipt)) as cur:
        receipts = await (await cur.execute(query, params)).fetchall()
    items = []
    for receipt in receipts:
        items.append(await read_items(receipt.id, conn))
    return receipts, items


@db_conn
async def read_one(id: str, conn: AsyncConnection) -> (Receipt, list[ReceiptItem]):
    query = f"""
        SELECT *
        FROM receipt 
        WHERE id = %s;
        """
    params = (id,)
    async with conn.cursor(row_factory=class_row(Receipt)) as cur:
        receipt = await (await cur.execute(query, params)).fetchone()
    items = await read_items(receipt.id, conn)
    return receipt, items


@db_conn
async def delete(id: int, conn: AsyncConnection) -> bool:
    query = """
    DELETE FROM receipt
    WHERE id = %s;
    """
    params = (id,)
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def count(criteria: ReceiptCriteria, conn: AsyncConnection) -> int:
    query = f"""
        SELECT COUNT(*)
        FROM receipt 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"date_time >= %(start_date)s" if criteria.start_date is not None else "TRUE"} AND 
        {"date_time <= %(end_date)s" if criteria.end_date is not None else "TRUE"} AND 
        {("(cashier_id LIKE %(query)s OR "
          "customer_card_id LIKE %(query)s)") if criteria.query is not None else "TRUE "};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res
