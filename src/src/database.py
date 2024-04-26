from psycopg_pool import AsyncConnectionPool

from config import DB_URL

pool = AsyncConnectionPool(DB_URL, open=False)


def db_conn(f):
    async def db_conn_(*args, **kwargs):
        async with pool.connection() as conn:
            return await f(*args, **kwargs, conn=conn)
    return db_conn_
