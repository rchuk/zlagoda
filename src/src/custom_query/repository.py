from psycopg import AsyncConnection
from psycopg.rows import class_row

from custom_query.schemas import (
    CustomQueryA1Request,
    CustomQueryA1Response,
    CustomQueryA2Request,
    CustomQueryA2Response,
    CustomQueryR1Request,
    CustomQueryR1Response,
    CustomQueryR2Request,
    CustomQueryR2Response,
    CustomQueryD1Request,
    CustomQueryD1Response,
    CustomQueryD2Request,
    CustomQueryD2Response
)
from database import db_conn


@db_conn
async def query_a1(request: CustomQueryA1Request, conn: AsyncConnection) -> CustomQueryA1Response:
    pass


@db_conn
async def query_a2(request: CustomQueryA2Request, conn: AsyncConnection) -> CustomQueryA2Response:
    pass


@db_conn
async def query_r1(request: CustomQueryR1Request, conn: AsyncConnection) -> CustomQueryR1Response:
    pass


@db_conn
async def query_r2(request: CustomQueryR2Request, conn: AsyncConnection) -> CustomQueryR2Response:
    pass


@db_conn
async def query_d1(request: CustomQueryR1Request, conn: AsyncConnection) -> CustomQueryD1Response:
    pass


@db_conn
async def query_d2(request: CustomQueryR2Request, conn: AsyncConnection) -> CustomQueryD2Response:
    pass
