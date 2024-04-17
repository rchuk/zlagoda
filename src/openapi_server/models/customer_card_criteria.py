from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class CustomerCardCriteria(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, sort_field=None, sort_ascending=None, last_name=None, phone_number=None, query=None):  # noqa: E501
        """CustomerCardCriteria - a model defined in OpenAPI

        :param offset: The offset of this CustomerCardCriteria.  # noqa: E501
        :type offset: int
        :param limit: The limit of this CustomerCardCriteria.  # noqa: E501
        :type limit: int
        :param sort_field: The sort_field of this CustomerCardCriteria.  # noqa: E501
        :type sort_field: str
        :param sort_ascending: The sort_ascending of this CustomerCardCriteria.  # noqa: E501
        :type sort_ascending: bool
        :param last_name: The last_name of this CustomerCardCriteria.  # noqa: E501
        :type last_name: str
        :param phone_number: The phone_number of this CustomerCardCriteria.  # noqa: E501
        :type phone_number: str
        :param query: The query of this CustomerCardCriteria.  # noqa: E501
        :type query: str
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'sort_field': str,
            'sort_ascending': bool,
            'last_name': str,
            'phone_number': str,
            'query': str
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'sort_field': 'sortField',
            'sort_ascending': 'sortAscending',
            'last_name': 'lastName',
            'phone_number': 'phoneNumber',
            'query': 'query'
        }

        self._offset = offset
        self._limit = limit
        self._sort_field = sort_field
        self._sort_ascending = sort_ascending
        self._last_name = last_name
        self._phone_number = phone_number
        self._query = query

    @classmethod
    def from_dict(cls, dikt) -> 'CustomerCardCriteria':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CustomerCardCriteria of this CustomerCardCriteria.  # noqa: E501
        :rtype: CustomerCardCriteria
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self) -> int:
        """Gets the offset of this CustomerCardCriteria.


        :return: The offset of this CustomerCardCriteria.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset: int):
        """Sets the offset of this CustomerCardCriteria.


        :param offset: The offset of this CustomerCardCriteria.
        :type offset: int
        """

        self._offset = offset

    @property
    def limit(self) -> int:
        """Gets the limit of this CustomerCardCriteria.


        :return: The limit of this CustomerCardCriteria.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        """Sets the limit of this CustomerCardCriteria.


        :param limit: The limit of this CustomerCardCriteria.
        :type limit: int
        """

        self._limit = limit

    @property
    def sort_field(self) -> str:
        """Gets the sort_field of this CustomerCardCriteria.


        :return: The sort_field of this CustomerCardCriteria.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field: str):
        """Sets the sort_field of this CustomerCardCriteria.


        :param sort_field: The sort_field of this CustomerCardCriteria.
        :type sort_field: str
        """

        self._sort_field = sort_field

    @property
    def sort_ascending(self) -> bool:
        """Gets the sort_ascending of this CustomerCardCriteria.


        :return: The sort_ascending of this CustomerCardCriteria.
        :rtype: bool
        """
        return self._sort_ascending

    @sort_ascending.setter
    def sort_ascending(self, sort_ascending: bool):
        """Sets the sort_ascending of this CustomerCardCriteria.


        :param sort_ascending: The sort_ascending of this CustomerCardCriteria.
        :type sort_ascending: bool
        """

        self._sort_ascending = sort_ascending

    @property
    def last_name(self) -> str:
        """Gets the last_name of this CustomerCardCriteria.


        :return: The last_name of this CustomerCardCriteria.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this CustomerCardCriteria.


        :param last_name: The last_name of this CustomerCardCriteria.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def phone_number(self) -> str:
        """Gets the phone_number of this CustomerCardCriteria.


        :return: The phone_number of this CustomerCardCriteria.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        """Sets the phone_number of this CustomerCardCriteria.


        :param phone_number: The phone_number of this CustomerCardCriteria.
        :type phone_number: str
        """

        self._phone_number = phone_number

    @property
    def query(self) -> str:
        """Gets the query of this CustomerCardCriteria.


        :return: The query of this CustomerCardCriteria.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query: str):
        """Sets the query of this CustomerCardCriteria.


        :param query: The query of this CustomerCardCriteria.
        :type query: str
        """

        self._query = query
