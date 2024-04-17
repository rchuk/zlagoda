import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.customer_card import CustomerCard  # noqa: E501
from openapi_server.models.customer_card_criteria import CustomerCardCriteria  # noqa: E501
from openapi_server.models.customer_card_view import CustomerCardView  # noqa: E501
from openapi_server import util


def count_customer_card(criteria=None):  # noqa: E501
    """Count customer cards

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  CustomerCardCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_customer_card(customer_card_view):  # noqa: E501
    """Create a new customer card

     # noqa: E501

    :param customer_card_view: 
    :type customer_card_view: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        customer_card_view = CustomerCardView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_customer_card(id):  # noqa: E501
    """Delete a customer card by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_customer_card_by_id(id):  # noqa: E501
    """Get customer card by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[CustomerCard, Tuple[CustomerCard, int], Tuple[CustomerCard, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_customer_card_list(criteria=None):  # noqa: E501
    """Get list of customer cards

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[List[CustomerCard], Tuple[List[CustomerCard], int], Tuple[List[CustomerCard], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  CustomerCardCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_customer_card(id, customer_card_view):  # noqa: E501
    """Update existing customer card

     # noqa: E501

    :param id: 
    :type id: int
    :param customer_card_view: 
    :type customer_card_view: dict | bytes

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        customer_card_view = CustomerCardView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
