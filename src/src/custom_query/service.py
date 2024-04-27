from custom_query import repository
from custom_query.schemas import (
    CustomQueryRequestBase,
    CustomQueryResponseBase
)
from exceptions import ValidationError


async def run_query(name: str, request: CustomQueryRequestBase) -> CustomQueryResponseBase:
    queries = {
        "a1": repository.query_a1,
        "a2": repository.query_a2,
        "r1": repository.query_r1,
        "r2": repository.query_r2,
        "d1": repository.query_d1,
        "d2": repository.query_d2
    }

    query = queries.get(name)
    if query is None:
        raise ValidationError("Вказаного запиту не існує")

    return await query(request)
