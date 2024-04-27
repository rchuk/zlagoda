from psycopg import AsyncConnection
from psycopg.rows import class_row

from product.models import Product
from product.schemas import ProductCriteria
from database import db_conn
from exceptions import ValidationError
from utils import like_format


def dto_field_to_entity_field(dto_field: str | None) -> str:
    if dto_field is None:
        return "upc"

    fields = {
        "id": "p.upc",
        "discountId": "p.discount_id",
        "archetype": "pa.name",
        "price": "p.price",
        "quantity": "p.quantity",
        "hasDiscount": "p.has_discount"
    }

    entity_field = fields.get(dto_field)
    if entity_field is None:
        raise ValidationError("Вказане поле для сортування не вірне")

    return entity_field

@db_conn
async def create(model: Product, conn: AsyncConnection) -> str:
    query = """
        INSERT INTO product(upc, discount_id, archetype, price, quantity, has_discount)
        VALUES (%(upc)s, %(discount_id)s, %(archetype)s, %(price)s, %(quantity)s, %(has_discount)s)
        RETURNING upc;
        """
    params = model.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res


@db_conn
async def read(criteria: ProductCriteria, conn: AsyncConnection) -> list[Product]:
    sort_field = dto_field_to_entity_field(criteria.sort_field)
    query = f"""
        SELECT 
        p.upc as upc, 
        p.discount_id as discount_id,
        p.archetype as archetype,
        p.price as price,
        p.quantity as quantity,
        p.has_discount as has_discount
        FROM 
        (product p INNER JOIN public.product_archetype pa on p.archetype = pa.id)
        WHERE 
        {"p.upc = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"p.archetype = %(archetype)s" if criteria.archetype is not None else "TRUE"} AND 
        {"p.has_discount = %(has_discount)s" if criteria.has_discount is not None else "TRUE"} AND 
        {("(p.upc LIKE %(query)s OR "
          "p.discount_id LIKE %(query)s OR "
          "pa.name LIKE %(query)s) ") if criteria.query is not None else "TRUE "}
        ORDER BY {sort_field} {'ASC ' if criteria.sort_ascending is None or criteria.sort_ascending else 'DESC '}
        {'LIMIT %(limit)s OFFSET %(offset)s ' if criteria.limit is not None and criteria.offset is not None else ''};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor(row_factory=class_row(Product)) as cur:
        res = await (await cur.execute(query, params)).fetchall()
    return res


@db_conn
async def read_one(id: str, conn: AsyncConnection) -> Product:
    query = f"""
        SELECT *
        FROM product 
        WHERE upc = %s;
        """
    params = (id,)
    async with conn.cursor(row_factory=class_row(Product)) as cur:
        res = await (await cur.execute(query, params)).fetchone()
    return res


@db_conn
async def update(model: Product, conn: AsyncConnection) -> bool:
    query = """
    UPDATE product
    SET 
    discount_id = %(discount_id)s,
    archetype = %(archetype)s,
    price = %(price)s,
    quantity = %(quantity)s,
    has_discount = %(has_discount)s
    WHERE upc = %(upc)s;
    """
    params = model.dict()
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def delete(id: str, conn: AsyncConnection) -> bool:
    query = """
    DELETE FROM product
    WHERE upc = %s;
    """
    params = (id,)
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def count(criteria: ProductCriteria, conn: AsyncConnection) -> int:
    query = f"""
        SELECT COUNT(*)
        FROM 
        (product p INNER JOIN public.product_archetype pa on p.archetype = pa.id)
        WHERE 
        {"p.upc = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"p.archetype = %(archetype)s" if criteria.archetype is not None else "TRUE"} AND 
        {"p.has_discount = %(has_discount)s" if criteria.has_discount is not None else "TRUE"} AND 
        {("p.upc LIKE %(query)s OR "
          "p.discount_id LIKE %(query)s OR "
          "pa.name LIKE %(query)s") if criteria.query is not None else "TRUE "};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res
