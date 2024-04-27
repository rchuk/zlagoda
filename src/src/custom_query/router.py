from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from custom_query.schemas import (
    CustomQueryRequestBase,
    CustomQueryResponseBase
)

from custom_query import service

router = APIRouter()


@router.post("/api/custom-query/{name}")
async def custom_query(
    name: Annotated[str, Path()],
    request: Annotated[CustomQueryRequestBase | None, Body()] = None,
) -> CustomQueryResponseBase:
    return await service.run_query(name, request)


