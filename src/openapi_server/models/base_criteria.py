from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class BaseCriteria(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sort_field=None, sort_ascending=None, offset=None, limit=None):  # noqa: E501
        """BaseCriteria - a model defined in OpenAPI

        :param sort_field: The sort_field of this BaseCriteria.  # noqa: E501
        :type sort_field: str
        :param sort_ascending: The sort_ascending of this BaseCriteria.  # noqa: E501
        :type sort_ascending: bool
        :param offset: The offset of this BaseCriteria.  # noqa: E501
        :type offset: int
        :param limit: The limit of this BaseCriteria.  # noqa: E501
        :type limit: int
        """
        self.openapi_types = {
            'sort_field': str,
            'sort_ascending': bool,
            'offset': int,
            'limit': int
        }

        self.attribute_map = {
            'sort_field': 'sortField',
            'sort_ascending': 'sortAscending',
            'offset': 'offset',
            'limit': 'limit'
        }

        self._sort_field = sort_field
        self._sort_ascending = sort_ascending
        self._offset = offset
        self._limit = limit

    @classmethod
    def from_dict(cls, dikt) -> 'BaseCriteria':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BaseCriteria of this BaseCriteria.  # noqa: E501
        :rtype: BaseCriteria
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sort_field(self) -> str:
        """Gets the sort_field of this BaseCriteria.


        :return: The sort_field of this BaseCriteria.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field: str):
        """Sets the sort_field of this BaseCriteria.


        :param sort_field: The sort_field of this BaseCriteria.
        :type sort_field: str
        """

        self._sort_field = sort_field

    @property
    def sort_ascending(self) -> bool:
        """Gets the sort_ascending of this BaseCriteria.


        :return: The sort_ascending of this BaseCriteria.
        :rtype: bool
        """
        return self._sort_ascending

    @sort_ascending.setter
    def sort_ascending(self, sort_ascending: bool):
        """Sets the sort_ascending of this BaseCriteria.


        :param sort_ascending: The sort_ascending of this BaseCriteria.
        :type sort_ascending: bool
        """

        self._sort_ascending = sort_ascending

    @property
    def offset(self) -> int:
        """Gets the offset of this BaseCriteria.


        :return: The offset of this BaseCriteria.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset: int):
        """Sets the offset of this BaseCriteria.


        :param offset: The offset of this BaseCriteria.
        :type offset: int
        """

        self._offset = offset

    @property
    def limit(self) -> int:
        """Gets the limit of this BaseCriteria.


        :return: The limit of this BaseCriteria.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        """Sets the limit of this BaseCriteria.


        :param limit: The limit of this BaseCriteria.
        :type limit: int
        """

        self._limit = limit
