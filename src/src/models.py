from pydantic import BaseModel, Field


class SortCriteria(BaseModel):
    """
    Sort Criteria
    """
    sort_field: str | None = Field(default=None, alias="sortField")
    sort_ascending: bool | None = Field(default=None, alias="sortAscending")


class BaseCriteria(SortCriteria):
    """
    Sort Criteria + Pagination
    """
    offset: int | None = None
    limit: int | None = None
    ids: list
