from psycopg import AsyncConnection
from psycopg.rows import class_row

from product_archetype.models import ProductArchetype
from product_archetype.schemas import ProductArchetypeCriteria
from database import db_conn
from exceptions import ValidationError
from utils import like_format


def dto_field_to_entity_field(dto_field: str | None) -> str:
    if dto_field is None:
        return "id"

    fields = {
        "id": "id",
        "category": "category",
        "name": "name",
        "manufacturer": "manufacturer",
        "description": "description"
    }

    entity_field = fields.get(dto_field)
    if entity_field is None:
        raise ValidationError("Вказане поле для сортування не вірне")

    return entity_field

@db_conn
async def create(model: ProductArchetype, conn: AsyncConnection) -> int:
    query = """
        INSERT INTO product_archetype(category, name, manufacturer, description)
        VALUES (%(category)s, %(name)s, %(manufacturer)s, %(description)s)
        RETURNING id;
        """
    params = model.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res


@db_conn
async def read(criteria: ProductArchetypeCriteria, conn: AsyncConnection) -> list[ProductArchetype]:
    sort_field = dto_field_to_entity_field(criteria.sort_field)
    query = f"""
        SELECT *
        FROM product_archetype 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"category = %(category)s" if criteria.category is not None else "TRUE"} AND 
        {("(name LIKE %(query)s OR "
          "manufacturer LIKE %(query)s OR "
          "description LIKE %(query)s) ") if criteria.query is not None else "TRUE "}
        ORDER BY {sort_field} {'ASC ' if criteria.sort_ascending is None or criteria.sort_ascending else 'DESC '}
        {'LIMIT %(limit)s OFFSET %(offset)s ' if criteria.limit is not None and criteria.offset is not None else ''};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor(row_factory=class_row(ProductArchetype)) as cur:
        res = await (await cur.execute(query, params)).fetchall()
    return res


@db_conn
async def read_one(id: int, conn: AsyncConnection) -> ProductArchetype:
    query = f"""
        SELECT *
        FROM product_archetype 
        WHERE id = %s;
        """
    params = (id,)
    async with conn.cursor(row_factory=class_row(ProductArchetype)) as cur:
        res = await (await cur.execute(query, params)).fetchone()
    return res


@db_conn
async def update(model: ProductArchetype, conn: AsyncConnection) -> bool:
    query = """
    UPDATE product_archetype
    SET 
    category = %(category)s,
    name = %(name)s,
    manufacturer = %(manufacturer)s,
    description = %(description)s
    WHERE id = %(id)s;
    """
    params = model.dict()
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def delete(id: int, conn: AsyncConnection) -> bool:
    query = """
    DELETE FROM product_archetype
    WHERE id = %s;
    """
    params = (id,)
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def count(criteria: ProductArchetypeCriteria, conn: AsyncConnection) -> int:
    query = f"""
        SELECT COUNT(*)
        FROM product_archetype
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"category = %(category)s" if criteria.category is not None else "TRUE"} AND 
        {("(name LIKE %(query)s OR "
          "manufacturer LIKE %(query)s OR "
          "description LIKE %(query)s)") if criteria.query is not None else "TRUE"};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res
