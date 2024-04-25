from psycopg_pool import AsyncConnectionPool

from config import DB_URL

pool = AsyncConnectionPool(DB_URL, open=False)


def db_conn(f):
    def db_conn_():
        async with pool.connection() as conn:
            f(conn=conn)

    return db_conn_
