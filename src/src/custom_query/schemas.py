from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field

from schemas import ListResponse, BaseCriteria


class CustomQueryRequestBase(BaseModel):
    pass


class CustomQueryResponseBase(BaseModel):
    pass


class CustomQueryA1Request(CustomQueryRequestBase):
    pass


class CustomQueryA1Response(CustomQueryResponseBase):
    pass


class CustomQueryA2Request(CustomQueryRequestBase):
    pass


class CustomQueryA2Response(CustomQueryResponseBase):
    pass


class CustomQueryR1Request(CustomQueryRequestBase):
    pass


class CustomQueryR1Response(CustomQueryResponseBase):
    pass


class CustomQueryR2Request(CustomQueryRequestBase):
    pass


class CustomQueryR2Response(CustomQueryResponseBase):
    pass


class CustomQueryD1Request(CustomQueryRequestBase):
    pass


class CustomQueryD1Response(CustomQueryResponseBase):
    pass


class CustomQueryD2Request(CustomQueryRequestBase):
    pass


class CustomQueryD2Response(CustomQueryResponseBase):
    pass
