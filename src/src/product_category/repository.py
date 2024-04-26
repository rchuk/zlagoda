from psycopg import AsyncConnection
from psycopg.rows import class_row

from product_category.models import ProductCategory
from product_category.schemas import ProductCategoryCriteria
from database import db_conn
from exceptions import ValidationError
from utils import like_format


def dto_field_to_entity_field(dto_field: str | None) -> str:
    if dto_field is None:
        return "id"

    fields = {
        "id": "id",
        "name": "name"
    }

    entity_field = fields.get(dto_field)
    if entity_field is None:
        raise ValidationError("Вказане поле для сортування не вірне")

    return entity_field

@db_conn
async def create(model: ProductCategory, conn: AsyncConnection) -> int:
    query = """
        INSERT INTO product_category(name)
        VALUES (%(name)s)
        RETURNING id;
        """
    params = model.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res


@db_conn
async def read(criteria: ProductCategoryCriteria, conn: AsyncConnection) -> list[ProductCategory]:
    sort_field = dto_field_to_entity_field(criteria.sort_field)
    query = f"""
        SELECT *
        FROM product_category 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"name LIKE %(query)s " if criteria.query is not None else "TRUE "}
        ORDER BY {sort_field} {'ASC ' if criteria.sort_ascending is None or criteria.sort_ascending else 'DESC '}
        {'LIMIT %(limit)s OFFSET %(offset)s ' if criteria.limit is not None and criteria.offset is not None else ''};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor(row_factory=class_row(ProductCategory)) as cur:
        res = await (await cur.execute(query, params)).fetchall()
    return res


@db_conn
async def read_one(id: int, conn: AsyncConnection) -> ProductCategory:
    query = f"""
        SELECT *
        FROM product_category 
        WHERE id = %s;
        """
    params = (id,)
    async with conn.cursor(row_factory=class_row(ProductCategory)) as cur:
        res = await (await cur.execute(query, params)).fetchone()
    return res


@db_conn
async def update(model: ProductCategory, conn: AsyncConnection) -> bool:
    query = """
    UPDATE product_category
    SET 
    name = %(name)s
    WHERE id = %(id)s;
    """
    params = model.dict()
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def delete(id: int, conn: AsyncConnection) -> bool:
    query = """
    DELETE FROM product_category
    WHERE id = %s;
    """
    params = (id,)
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def count(criteria: ProductCategoryCriteria, conn: AsyncConnection) -> int:
    query = f"""
        SELECT COUNT(*)
        FROM product_category 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"name LIKE %(query)s " if criteria.query is not None else "TRUE"};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res
