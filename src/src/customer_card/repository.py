from psycopg import AsyncConnection
from psycopg.rows import class_row

from customer_card.models import CustomerCard
from customer_card.schemas import CustomerCardCriteria
from database import db_conn
from utils import like_format, generate_random_str_id


@db_conn
async def create(model: CustomerCard, conn: AsyncConnection) -> str:
    model.id = generate_random_str_id(13)
    query = """
        INSERT INTO customer_card(id, last_name, first_name, patronymic, phone_number, city, street, zip_code, discount_percent)
        VALUES (%(id)s, %(last_name)s, %(first_name)s, %(patronymic)s, %(phone_number)s, %(city)s, %(street)s, %(zip_code)s, %(discount_percent)s)
        RETURNING id;
        """
    params = model.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res


@db_conn
async def read(criteria: CustomerCardCriteria, conn: AsyncConnection) -> list[CustomerCard]:
    query = f"""
        SELECT *
        FROM customer_card 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"discount_percent = %(discount_percent)s" if criteria.discount_percent is not None else "TRUE"} AND 
        {("(last_name LIKE %(query)s OR "
          "first_name LIKE %(query)s OR "
          "patronymic LIKE %(query)s OR "
          "phone_number LIKE %(query)s OR "
          "city LIKE %(query)s OR "
          "street LIKE %(query)s OR "
          "zip_code LIKE %(query)s)") if criteria.query is not None else "TRUE"}
        {(f"ORDER BY %(sort_field) {'ASC' if criteria.sort_ascending is None or criteria.sort_ascending else 'DESC'}"
          f"{'LIMIT %(limit)s OFFSET %(offset)s' if criteria.limit is not None and criteria.offset is not None else ''}")
    if criteria.sort_field is not None else ""};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor(row_factory=class_row(CustomerCard)) as cur:
        res = await (await cur.execute(query, params)).fetchall()
    return res


@db_conn
async def read_one(id: str, conn: AsyncConnection) -> CustomerCard:
    query = f"""
        SELECT *
        FROM customer_card 
        WHERE id = %s;
        """
    params = (id,)
    async with conn.cursor(row_factory=class_row(CustomerCard)) as cur:
        res = await (await cur.execute(query, params)).fetchone()
    return res


@db_conn
async def update(model: CustomerCard, conn: AsyncConnection) -> bool:
    query = """
    UPDATE customer_card
    SET 
    last_name = %(last_name)s,
    first_name = %(first_name)s,
    patronymic = %(patronymic)s,
    phone_number = %(phone_number)s,
    city = %(city)s,
    street = %(street)s,
    zip_code = %(zip_code)s,
    discount_percent = %(discount_percent)s
    WHERE id = %(id)s;
    """
    params = model.dict()
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def delete(id: str, conn: AsyncConnection) -> bool:
    query = """
    DELETE FROM customer_card
    WHERE id = %s;
    """
    params = (id,)
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def count(criteria: CustomerCardCriteria, conn: AsyncConnection) -> int:
    query = f"""
        SELECT COUNT(*)
        FROM customer_card 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"discount_percent = %(discount_percent)s" if criteria.discount_percent is not None else "TRUE"} AND
        {("(last_name LIKE %(query)s OR "
          "first_name LIKE %(query)s OR "
          "patronymic LIKE %(query)s OR "
          "phone_number LIKE %(query)s OR "
          "city LIKE %(query)s OR "
          "street LIKE %(query)s OR "
          "zip_code LIKE %(query)s)") if criteria.query is not None else "TRUE"};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res
