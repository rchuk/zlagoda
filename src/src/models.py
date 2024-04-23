from typing import Annotated

from pydantic import BaseModel, Field


class SortCriteria(BaseModel):
    """
    Sort Criteria
    """
    sort_field: Annotated[str | None, Field(alias="sortField")] = None
    sort_ascending: Annotated[bool | None, Field(alias="sortAscending")] = None


class BaseCriteria(SortCriteria):
    """
    Sort Criteria + Pagination
    """
    offset: int | None = None
    limit: int | None = None
    ids: list
