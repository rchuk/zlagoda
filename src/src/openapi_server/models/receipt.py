# coding: utf-8

"""
    Zlagoda

    API for systems used by the employees of Zlagoda shops

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.receipt_item import ReceiptItem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Receipt(BaseModel):
    """
    Receipt
    """ # noqa: E501
    id: StrictInt
    cashier_id: StrictInt = Field(alias="cashierId")
    customer_card_id: Optional[StrictInt] = Field(default=None, alias="customerCardId")
    date_time: datetime = Field(alias="dateTime")
    total_price: StrictInt = Field(alias="totalPrice")
    vat: StrictInt
    items: List[ReceiptItem]
    __properties: ClassVar[List[str]] = ["id", "cashierId", "customerCardId", "dateTime", "totalPrice", "vat", "items"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Receipt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Receipt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "cashierId": obj.get("cashierId"),
            "customerCardId": obj.get("customerCardId"),
            "dateTime": obj.get("dateTime"),
            "totalPrice": obj.get("totalPrice"),
            "vat": obj.get("vat"),
            "items": [ReceiptItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None
        })
        return _obj


