from psycopg import AsyncConnection
from psycopg.rows import class_row

from auth.models import User
from auth.schemas import UserCriteria
from database import db_conn


@db_conn
async def create(model: User, conn: AsyncConnection) -> str:
    query = """
        INSERT INTO users(login, password_hash, role_id, employee_id)
        VALUES (%(login)s, %(password_hash)s, %(role_id)s, %(employee_id)s)
        RETURNING login;
        """
    params = model.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res


@db_conn
async def read_one(login: str, conn: AsyncConnection) -> User:
    query = f"""
        SELECT *
        FROM users 
        WHERE login = %s;
        """
    params = (login,)
    async with conn.cursor(row_factory=class_row(User)) as cur:
        res = await (await cur.execute(query, params)).fetchone()
    return res


@db_conn
async def read(criteria: UserCriteria, conn: AsyncConnection) -> list[User]:
    query = f"""
        SELECT *
        FROM users 
        WHERE 
        {"login = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {'LIMIT %(limit)s OFFSET %(offset)s ' if criteria.limit is not None and criteria.offset is not None else ''};
        """
    params = criteria.dict()
    async with conn.cursor(row_factory=class_row(User)) as cur:
        res = await (await cur.execute(query, params)).fetchall()
    return res


@db_conn
async def update(model: User, conn: AsyncConnection) -> bool:
    query = """
    UPDATE users
    SET
    password_hash = %(password_hash)s,
    role_id = %(role_id)s,
    employee_id = %(employee_id)s
    WHERE login = %(login)s;
    """
    params = model.dict()
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def delete(login: str, conn: AsyncConnection) -> bool:
    query = """
    DELETE FROM users
    WHERE login = %s;
    """
    params = (login,)
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def count(criteria: UserCriteria, conn: AsyncConnection) -> int:
    query = f"""
        SELECT COUNT(*)
        FROM users;
        """
    params = criteria.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res


@db_conn
async def role_map(id: str, conn: AsyncConnection) -> str:
    query = f"""
        SELECT name
        FROM roles 
        WHERE id = %s;
        """
    params = (id,)
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res